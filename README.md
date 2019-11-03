gCodeLexer
==========

G-Code used to control CNC machines, such as mills, printers, and lathes.
This repository is enables synthax highlighting of such code with python's pygments library.

This feature has been missing in pygments. At some point this repo will be pushed upstream.


Documentation
------------
The online documention for pygments can be found on its homepage: https://pygments.org

This repository is recognizing the following file extensions as gcode to be lexed:
apt, cnc, din, dnc, ecs, eia, fan, fgc, fnc, gc, gcd, GCD, gcode, hnc, i, maz, min, mpf,
mpr, nc, NC, ncc, ncf, ncg, ncp, ngc, pim, plt, ply, prg, ptp, rol, sbp, tap, xpi

## INSTALL

    python setup.py install

## Usage

    from pygments.lexers import get_lexer_by_name
    get_lexer_by_name('gcode')

or

    from pygments.lexers import find_lexer_class
    find_lexer_class('gCodeLexer')


After installing, you can also run `pygmentize`. 

    pygmentize -O full -f html -o samples.html samples.ngc


## Sample

![A lexed gcode sample drawn with default styling](Sample.png?raw=true "Lexer Sample")
