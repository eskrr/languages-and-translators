# module: eskr_lex.py
# This module just contains the lexing rules

import ply.lex as lex

reserved = {
	'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'function' : 'FUNCTION',
    'int' : 'INT',
    'float' : 'FLOAT',
    'main' : 'MAIN',
    'cout' : 'COUT',
    'cin' : 'CIN',
    'endl': 'ENDL'
 }

tokens = [
	'LBRACE',
	'RBRACE',
	'LBRACKET',
	'RBRACKET',
	'SEMICOLON',
	'COMMA',
	'EQUAL',
	'DOT',
	'LPAREN',
	'RPAREN',
	'LESS_THAN',
	'LESS_OR_EQUAL_THAN',
	'EQUAL_THAN',
	'DIFFERENT_THAN',
	'GREATER_THAN',
	'GREATER_OR_EQUAL_THAN',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'MOD',
	'OR',
	'AND',
	'NOT',
	'NUMBER',
	'ID',
	'INSTREAM',
	'OUTSTREAM',
	'TEXT',
] + list(reserved.values())

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r'\,'
t_EQUAL = r'='
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LESS_THAN = r'<'
t_LESS_OR_EQUAL_THAN = r'<='
t_EQUAL_THAN = r'=='
t_DIFFERENT_THAN = r'!='
t_GREATER_THAN = r'>'
t_GREATER_OR_EQUAL_THAN = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_OUTSTREAM = r'<<'
t_INSTREAM = r'>>'
t_TEXT = r'"(.*?)"'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_COMMENT(t):
    r'\#.+'
    pass
    # No return value. Token discarded
 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
