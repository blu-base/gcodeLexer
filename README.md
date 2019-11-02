gCode Lexer
==========

G-Code used to control CNC machines, such as mills, printers, and lathes.
This repository is enables synthax highlighting of such code with python's pygments library.

This feature has been missing in pygments. At some point this repo will be pushed upstream.


Documentation
------------
The online documention for pygments can be found on its homepage: https://pygments.org


## INSTALL

    python setup.py install

## Usage

Use `GCodeLexer()` as drop-in replacement for `pygments.lexer` classes.

    from gCodeLexer import GCodeLexer


## Sample

![A lexed gcode sample drawn with default styling](Sample.png?raw=true "Lexer Sample")
