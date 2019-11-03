# -*- coding: utf-8 -*-
from pygments.lexer import RegexLexer, bygroups, words, include
from pygments.token import *

import re


__all__ = ['GCodeLexer']

class GCodeLexer(RegexLexer):
    """
    Lexer for gCode

    """
    name = 'gCodeLexer'
    aliases = ['gcode']


    fileextensions = ['apt', 'cnc', 'din', 'dnc', 'ecs', 'eia', 'fan', 
                      'fgc', 'fnc', 'gc', 'gcd', 'GCD', 'gcode', 'hnc', 
                      'i', 'maz', 'min', 'mpf', 'mpr', 'nc', 'NC', 'ncc', 
                      'ncf', 'ncg', 'ncp', 'ngc', 'pim', 'plt', 'ply', 'prg', 
                      'ptp', 'rol', 'sbp', 'tap', 'xpi']

    filenames = ['*.' + ext for ext in fileextensions] 

    # Builtin words
    builtins = (
        'if', 'endif', 'end_if'
        'then', 'else', 'elsif',
        'while', 'endwhile', 'end_while',
        'goto', 'exit',
        'sub', 'endsub', 'end_sub',
        'call',
        'repeat', 'endrepeat', 'end_repeat', 'until'
    )

    # Build in math functions
    functions = (
        'and', 'or','xor',
        'eq', 'ne', 'gt', 'ge', 'lt', 'le',
        'mod',
        'cos', 'sin', 'tan', 'acos', 'asin', 'atan',
        'abs', 'round', 'fix', 'fup', 'exists',
        'exp', 'ln', 'sqrt'
    )

    tokens = {
        'root': [
            
            # multi-line comments. Only for
            (r';', Comment.Multiline, 'comment'),
            (r'\(', Comment.Multiline, 'par_comment'),
            (r'\([^\n\r]*\)', Comment.SingleLine),

            # Braced expressions entry point
            # TODO 
            # make the bracing more intelligent, such as in tcl lexer
            (r'(\[)', Keyword, 'bracket'),

            # Line numbers
            (r'\s*[nN]\d+', Comment),
            # G and M commands and other tooling, match only the label
            (r'(?<![a-zA-Z\<])[gGmMhHdDtT](?=(\d+\.?\d?))', Keyword.Declaration),
            # Coordinates, Feeds, Speeds, and Machining parameter, 
            # match only the label
            (r'(?<![a-zA-Z\<])[xXyYzZiIjJkKlLpPqQrReEaAbBcCuUvVwWfFsS\^\@](?=(\s*[+-]?\d*\.?\d+|\s*[+-]?#))', Keyword.Type),


            # Non-persistent Arguments (#1-#30)
            (r'(?<=#)0*[1-3]?[0-9](?=\D)', Name.Variable.Magic),
            # Numbered Variables
            (r'(?<=#)0*[4-9]?[0-9]{1,5}', Name.Variable),
            # Local Variables
            (r'(?<=#\<)\w[\w_]*(?=\>)', Name.Variable),
            # GlobalVariables
            (r'(?<=#\<)_[\w_]*(?=\>)',Name.Variable.Global),

            # Variables Indicator
            (r'(#|\<|\>)', Name.Variable),

            # built in commands, match case-insensitive
            ("(?i)(%s)" % '|'.join(re.escape(entry) for entry in builtins), Name.Builtin),

            # math functions, math case-insensitive
            (r'[-+*/:=]', Operator),
            ("(?i)(%s)" % '|'.join(re.escape(entry) for entry in functions), Operator.Word),

            # Subroutines, match label
            (r'(?<![a-zA-Z\<])[oO](?=[\d\<\[])', Keyword.Reserved),
            # Subroutines, named, match function name
            (r'(?<=([oO][\<\[]))\w+(?=\>)', Name.Function),

            # OTHERS
            include('data')

        ],
        'data':[
            (r'\s+', Text),
            (r'\d?\.\d+', Number.Float),
            (r'\d+', Number.Integer),
            (r'\w+', Text),
        ],
        'par_comment':[
            (r'[^()]', Comment.Multiline),
            (r'\(', Comment.Multiline, '#push'),
            (r'\)', Comment.Multiline, '#pop'),
            (r'\)', Comment.Multiline),
        ],
        'comment':[
             (r'.*;.*$', Comment.Multiline, '#pop'),
             (r'^.*\n', Comment.Multiline),
             (r'.', Comment.Multiline),
        ],

        'bracket': [
            (r'\]', Keyword, '#pop'),
            include('root')
        ],
    }

