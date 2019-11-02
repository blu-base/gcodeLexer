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

    from pygments.lexers import get_lexer_by_name
    get_lexer_by_name('gcode')

or
    from pygments.lexers import find_lexer_class
    find_lexer_class('gCodeLexer')


## Sample

![A lexed gcode sample drawn with default styling](Sample.png?raw=true "Lexer Sample")
