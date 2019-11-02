from setuptools import setup

setup(
    name='gCodeLexer',
    version='0.1',
    description='Pygments lexer for G-Code files',
    author='Sebastian Engel',
    url='https://github.com/blu-base/gcodeLexer/',
    packages=['gCodeLexer'],
    entry_points='''[pygments.lexers]
    gCodeLexer = gCodeLexer:GCodeLexer
'''
)
