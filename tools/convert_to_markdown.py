#!/usr/bin/env python3
"""Convert the ACE LaTeX specification to GitHub-flavored Markdown."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ENTRYPOINT = ROOT / "tools" / "markdown.tex"
FILTER = ROOT / "tools" / "markdown.lua"

INPUT_RE = re.compile(r"^[ \t]*\\input\{([^}]+)\}[ \t]*$", re.MULTILINE)
TABLE_ENVIRONMENTS = {
    "table",
    "NXSTable",
    "JXSTable",
    "BlockTable",
    "XSSTable",
    "LAWTable",
    "LOCTable",
}
ENVIRONMENT_RE = re.compile(r"\\(begin|end)\{([^}]+)\}")
DISPLAY_MATH_RE = re.compile(
    r"\\begin\{(equation|align\*?|multline\*?)\}(.*?)\\end\{\1\}",
    re.DOTALL,
)


def expand_inputs(path: Path, active: tuple[Path, ...] = ()) -> str:
    """Inline LaTeX input files so source normalization is non-destructive."""
    path = path.resolve()
    if path in active:
        cycle = " -> ".join(str(item) for item in (*active, path))
        raise ValueError(f"cyclic LaTeX input: {cycle}")

    text = path.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        child = (path.parent / match.group(1)).resolve()
        if child.suffix == "":
            child = child.with_suffix(".tex")
        return expand_inputs(child, (*active, path))

    return INPUT_RE.sub(replace, text)


def normalize_alias_references(text: str) -> str:
    """Point secondary labels on one heading at Pandoc's primary label."""
    aliases: dict[str, str] = {}
    for line in text.splitlines():
        if not re.search(
            r"\\(?:section|subsection|subsubsection|subsubsubsection|paragraph)",
            line,
        ):
            continue
        labels = re.findall(r"\\label\{(sec:[^}]+)\}", line)
        if len(labels) > 1:
            aliases.update({label: labels[0] for label in labels[1:]})

    for alias, primary in aliases.items():
        text = text.replace(
            rf"\Sectionref{{{alias}}}",
            rf"\Sectionref{{{primary}}}",
        )
        text = text.replace(rf"\ref{{{alias}}}", rf"\ref{{{primary}}}")
    return text


def normalize_table_references(text: str) -> str:
    """Give every table a stable HTML anchor and explicit reference number."""
    stack: list[tuple[str, int, int]] = []
    edits: list[tuple[int, int, str]] = []
    table_numbers: dict[str, int] = {}
    table_number = 0

    for match in ENVIRONMENT_RE.finditer(text):
        action, environment = match.groups()
        if environment not in TABLE_ENVIRONMENTS:
            continue
        if action == "begin":
            table_number += 1
            stack.append((environment, match.start(), table_number))
            continue
        if not stack or stack[-1][0] != environment:
            raise ValueError(f"unbalanced table environment: {environment}")

        _, begin, number = stack.pop()
        body = text[begin : match.end()]
        labels = list(re.finditer(r"\\label\{(tab:[^}]+)\}", body))
        for label_match in labels:
            label = label_match.group(1)
            table_numbers[label] = number
            edits.append(
                (
                    begin + label_match.start(),
                    begin + label_match.end(),
                    "",
                )
            )
            edits.append((begin, begin, rf"\hypertarget{{{label}}}{{}}" + "\n"))

    if stack:
        raise ValueError(f"unclosed table environment: {stack[-1][0]}")

    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]

    for label, number in table_numbers.items():
        link = rf"\hyperref[{label}]{{{number}}}"
        text = text.replace(rf"\Tableref{{{label}}}", rf"Table~{link}")
        text = text.replace(rf"\ref{{{label}}}", link)
    return text


def normalize_display_math(text: str) -> str:
    """Convert numbered LaTeX environments to Markdown display math."""
    equation_number = 0
    equation_numbers: dict[str, int] = {}

    def replace(match: re.Match[str]) -> str:
        nonlocal equation_number
        environment, body = match.groups()
        numbered = not environment.endswith("*")
        if numbered:
            equation_number += 1

        labels = re.findall(r"\\label\{(eq:[^}]+)\}", body)
        body = re.sub(r"\s*\\label\{eq:[^}]+\}", "", body)
        anchors = ""
        for label in labels:
            equation_numbers[label] = equation_number
            anchors += rf"\hypertarget{{{label}}}{{}}" + "\n"

        body = re.sub(
            r"\\intertext\{([^{}]*)\}",
            lambda item: r"\\ \text{" + item.group(1) + r"} \\",
            body,
        ).strip()
        if environment.startswith(("align", "multline")):
            body = "\\begin{aligned}\n" + body + "\n\\end{aligned}"
        if numbered:
            body += rf"\tag{{{equation_number}}}"
        return anchors + "\\[\n" + body + "\n\\]"

    text = DISPLAY_MATH_RE.sub(replace, text)
    for label, number in equation_numbers.items():
        link = rf"\hyperref[{label}]{{{number}}}"
        text = text.replace(rf"\Equationref{{{label}}}", rf"Equation~{link}")
        text = text.replace(rf"\ref{{{label}}}", link)
    return text


def normalize_latex(text: str) -> str:
    """Rewrite the few package-level constructs Pandoc cannot expand."""
    # LOC's second argument is optional but uses xparse's braced G argument,
    # which Pandoc does not implement. Expand the no-subscript form directly;
    # the remaining uses all have the second argument.
    text = re.sub(
        r"\\LOC\{([^{}]*)\}(?!\s*\{)",
        r"\\texttt{LOC\1}",
        text,
    )
    text = (
        "\\newcommand{\\LOC}[2]{\\ensuremath{\\mathtt{LOC#1}_{#2}}}\n"
        + text
    )

    # Package macros with optional arguments are similarly normalized.
    text = re.sub(
        r"\\isotope(?:\[([^\]]+)\])?\{([^{}]+)\}",
        lambda match: (
            rf"$^{{{match.group(1)}}}\mathrm{{{match.group(2)}}}$"
            if match.group(1)
            else match.group(2)
        ),
        text,
    )
    text = re.sub(
        r"\\todo(?:\[[^\]]*\])?\{([^{}]*)\}",
        r"\\textbf{TODO:} \1",
        text,
    )
    text = re.sub(r"\\cmidrule(?:\([^)]*\))?\{[^}]+\}", "", text)

    # Normalize the two package/custom column specifications used by otherwise
    # standard tabular environments.
    text = text.replace(r"{rVll}", r"{rlll}")
    text = text.replace(r"{rS[table-format = 1.3e1]|rS}", r"{rrrr}")
    text = normalize_alias_references(text)
    text = normalize_table_references(text)
    return normalize_display_math(text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=ROOT / "ACEFormat.md",
        help="output Markdown path (default: ACEFormat.md)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        print("error: pandoc is required but was not found on PATH", file=sys.stderr)
        return 2

    latex = normalize_latex(expand_inputs(ENTRYPOINT))
    args.output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="aceformat-markdown-") as temp_dir:
        normalized = Path(temp_dir) / "ACEFormat.normalized.tex"
        normalized.write_text(latex, encoding="utf-8")
        command = [
            pandoc,
            str(normalized),
            "--from=latex",
            "--to=gfm-tex_math_gfm+tex_math_dollars",
            "--output",
            str(args.output),
            "--bibliography",
            str(ROOT / "src" / "References.bib"),
            "--citeproc",
            "--number-sections",
            "--wrap=none",
            "--lua-filter",
            str(FILTER),
        ]
        subprocess.run(command, cwd=ROOT, check=True)

    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
