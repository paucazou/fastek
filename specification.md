# Fastek specifications
This document describes the specifications of the fastek language.
## Principles
### Errors
Fastek does not tolerate the least error. If an error occurs, the interpreter must stop and explain, as much as possible, the error to the user.
### Way to do things
There must be one, and only one way to do something.
## Shebang

## Main tags
They are two main root tags, two special tags and the end of line.
### Main root tags
Tag|Name|Example
---|-----|-------
,;|Opening root tag (ORT)|,;v
;;|Closing root tag (CRT)|;;bi


These tags are called roots because they must be followed by one or more letters, in order to form a complete tag. An opening tag can be followed by a closing tag only if the parser corresponding with the letters specifies it.


A root tag is followed by a letter, which refers to a specific parser. This letter can be followed by another one, and even more, but it is specific to each parser.

Spaces around the tags: 
* No space is allowed inside the tag, including between the root and the letters.
### EOL tag
Tag|Name|Example
---|-----|-------
,,|EOL tag|,,


The EOL tag indicates the end of the line. It must be preceded by a space, or a space-like, or the start of line, and followed by a space, a space-like or the end of line.

### Expand tag
Tag|Name|Example
---|-----|-------
::|Expand tag|::placeholder


The Expand tag is used to expand the data linked to the name which followed it. The Expand tag must be after a space, a space-like, a start of line, and followed by a name already linked to some data, itself followed by a space, a space-like or an end of line.

## Tags supported
Only the tags below are supposed to be corrects by the fastek interpreter. No other tag is allowed. However, it is possible to extend the number of tags supported by adding new parsers (see below : Improve fastek).


Tags are case sensitive. Tags which have no closing tags are closed by the end of the line.
### b: bold and other things of that kind
* b tags must be closed : ;;bi, ;;bu, ;;bb...
* b tag has following subtags :
  * i: italic. LaTeX: \italic{}
  * b: bold. LaTeX: \bold{}
  * u: underline. LaTeX: \underlined{}
### c: comments
* Comments must be closed : ;;c
* Comments have no subtags.
* Text inside c tags will not appear in output.
### e: environment
* e tags must be closed: ;;el, ;;er...
* e tag is equal to LaTeX \begin{} and \end{}. Environment names are limited to subtags.
* e tag has following subtags:
  * l: left. LaTeX: flushleft
  * r: right. LaTeX: flushright
  * c: center. LaTeX: center


**Warning**: many LaTeX environments are supported in fastek by others ways. For example, document environment is automatically created at compile time.
### f: footnote
* f tag must be closed.
* f tag can be used alone, and is equal to LaTeX \footnote{}.
* f tag has following subtags:
  * n: followed by a number, is equal to LaTeX \footnotemark[]
  * t: followed by a number, and at least one word, is equal to LaTeX \footnotetext[]{}
### l: list
* l tag has no closing tag.
* l tag only specifies items, and creates environmnents by detecting the first item, and closes it by detecting the last one.
* l tag has followings subtags:
  * u: unordered list. LaTeX: inside 'itemize' environment.
  * n: ordered list. LaTeX: inside 'enumerate' environment.
  * d: descriptive list. LaTeX: inside 'description' environment.

### o: box
### s: spaces
### t: title
* titles musn't be closed.
* t tag has following subtags:
  * c: chapter. LaTeX: \chapter{}
  * s: section. LaTeX: \section{}
  * u: subsection. LaTeX: \subsection{}
  * p: part. LaTeX: \part{}
  * h: paragraph. LaTeX: \paragraph{}
  * r: subparagraph. LaTeX: \subparagraph{}
* Not numbered titles can be created by adding '*' just after subtag. Example : ",;tc* A great thing", LaTeX: "\chapter*{A great thing}"


## Special tags

### Index

### Placeholder
### Latex tags
Latex tags may be directly included into fastek, but are not evaluated.

## Suffix
A fastek file must have a shebang in the first line but it is not absolutely mandatory. If it has nos shebang, however, it must have a specific suffix, which is '.ftk'.

## Improve Fastek
### Add new parsers
New parsers can be created easily.
