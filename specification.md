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
* an opening tag must come after a space, or the start of the line. It must be followed by a space, or an end of line.
* a closing tag must not come after a space (or space-like, like a tab) or the start of the line. It must be followed by a space, or an end of line.
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

## Detailed tags table

## Special tags

### Index

### Placeholder

## Suffix
A fastek file must have a shebang in the first line but it is not absolutely mandatory. If it has nos shebang, however, it must have a specific suffix, which is '.ftk'.
