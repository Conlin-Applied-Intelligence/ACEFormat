-- Small output cleanups that are easier and safer on Pandoc's parsed AST.

local function strip_color_commands(text)
  -- ACE examples use one non-nested \color{name}{line} command per line.
  return text:gsub("\\color%s*{[^}]+}%s*{([^}\n]*)}", "%1")
end

function CodeBlock(block)
  block.text = strip_color_commands(block.text)
  return block
end

function Code(code)
  code.text = strip_color_commands(code.text)
  return code
end

function Div(div)
  if div.classes:includes("center") then
    return div.content
  end
  if #div.content == 0 and div.identifier ~= "" then
    return pandoc.RawBlock(
      "html",
      '<a id="' .. div.identifier .. '"></a>'
    )
  end
end

function Span(span)
  if #span.content == 0 and span.identifier ~= "" then
    return pandoc.RawInline(
      "html",
      '<a id="' .. span.identifier .. '"></a>'
    )
  end
end

function Inlines(inlines)
  -- The source commonly places an em dash immediately after a block link:
  -- [label](#target)—description. Although valid CommonMark, some renderers
  -- fail to recognize the link boundary. Put spaces around that dash.
  local output = pandoc.List()
  for index, inline in ipairs(inlines) do
    local previous = inlines[index - 1]
    local previous_link = previous
    if previous
      and previous.tag == "Strong"
      and #previous.content == 1
      and previous.content[1].tag == "Link"
    then
      previous_link = previous.content[1]
    end
    if inline.tag == "Str"
      and inline.text:match("^—")
      and previous_link
      and previous_link.tag == "Link"
      and previous_link.target:match("^#sec:")
    then
      output:insert(pandoc.Space())
      output:insert(pandoc.Str("—"))
      local remainder = inline.text:sub(#"—" + 1)
      if remainder ~= "" then
        output:insert(pandoc.Space())
        output:insert(pandoc.Str(remainder))
      end
    else
      output:insert(inline)
    end
  end
  return output
end

function Header(header)
  -- Labels from the LaTeX source contain a namespace such as "sec:" or
  -- "par:". GitHub already generates anchors for ordinary unlabeled headings.
  if header.identifier:find(":", 1, true) then
    local anchor = pandoc.RawBlock(
      "html",
      '<a id="' .. header.identifier .. '"></a>'
    )
    return {anchor, header}
  end
end
