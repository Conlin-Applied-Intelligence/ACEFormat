# ACE&mdash;A Compact ENDF&mdash;Format Specification
This repository contains the specification for the ACE format&mdash;as well as a few supporting formats.

The information contained in this document was formerly Appendix F of the MCNP5 manual, but has been put in its own document to enable wider distribution. Currently the specification only contains a portion of the full specification. More will be added in time.

The document itself is [ACEFormat.pdf](ACEFormat.pdf) and can be downloaded/viewed without having to clone or download the entire repository.

Please note: **this document is not complete at this time.**

## About This Fork

This fork includes a conversion of the original ACE Format document to Markdown, making the specification easier for AI systems and other tools to consume. The original LaTeX sources remain authoritative, and the Markdown version is generated from them.

## Markdown

The Markdown version is generated from the LaTeX sources:

```sh
python3 tools/convert_to_markdown.py
```

The converter requires Pandoc and writes `ACEFormat.md`. Its compatibility entry point expands the custom ACE table environments into standard LaTeX tables before Pandoc converts them; `ACEFormat.md` should therefore not be edited by hand.

## Issues
If you discover problems with the specification, please [file an issue](https://github.com/NuclearData/ACEFormat/issues) on GitHub. This will allow those involved to investigate and keep a record of what has been done. Note that we are not modifying or extending the format at this time; we are only looking for bugs in the format specification.

# License
This format is covered under the license agreement contained in the [LICENSE](LICENSE) file.
