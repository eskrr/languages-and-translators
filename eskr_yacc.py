 # Yacc example
 
import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from eskr_lex import tokens

start = 'expression'
symbols_table = {}
operands_stack = []
operators_stack = []

def p_program(p):
  'program : program_block'
  global debug
  if debug:
    print('program')
    print(p.stack)
    print('\n')

def p_program_block(p):
  '''program_block : declaration SEMICOLON program_block 
                   | assignation SEMICOLON program_block
                   | normal_function program_block
                   | main_function'''
  global debug
  if debug:
    print('program_block')
    print(p.stack)
    print('\n')

def p_normal_function(p):
  'normal_function : FUNCTION ID LPAREN RPAREN function_block'
  global debug
  if debug:
    print('other function')
    print(p.stack)
    print('\n')

def p_main_function(p):
  'main_function : FUNCTION MAIN LPAREN RPAREN function_block'
  global debug
  if debug:
    print('MAIN')
    print(p.stack)
    print('\n')

def p_function_block(p):
  'function_block : LBRACE instruction RBRACE'
  global debug
  if debug:
    print('function block')
    print(p.stack)
    print('\n')

def p_instruction(p):
  '''instruction : proposition instruction
                 | empty'''
  global debug
  if debug:
    print('instruction')
    print(p.stack)
    print('\n')

def p_proposition(p):
  '''proposition : function_call SEMICOLON
                 | assignation SEMICOLON
                 | print SEMICOLON
                 | input SEMICOLON
                 | unary_operation SEMICOLON
                 | if_sentence
                 | while_sentence
                 | do_while_sentence
                 | for_sentence'''
  global debug
  if debug:
    print('proposition')
    print(p.stack)
    print('\n')

def p_print(p):
  '''print : COUT output_expression
     output_expression : OUTSTREAM expression output_expression
                       | OUTSTREAM expression
                       | OUTSTREAM TEXT output_expression
                       | OUTSTREAM TEXT
  '''

def p_input(p):
  '''input : CIN input_expression
     input_expression : INSTREAM id input_expression
                      | INSTREAM id
  '''

def p_declaration(p):
  '''declaration : type variables EQUAL expression
                 | type variables'''
  global debug
  global symbols_table
  for symbol in p[2]:
    if symbol not in symbols_table:
      symbols_table[symbol] = p[1]
    else:
      raise SyntaxError
  if debug:
    print('declaration')
    print(p.stack)
    print('\n')    

def p_type(p):
  '''type : INT
          | DOUBLE'''
  p[0] = p[1]

def p_assignation(p):
  '''assignation : variables EQUAL expression
                 | variables'''
  global debug
  if debug:
    print('assignation')
    print(p.stack)
    print('\n')


def p_unary_operation(p):
  '''unary_operation : ID PLUS PLUS
                     | ID MINUS MINUS
                     | PLUS PLUS ID
                     | MINUS MINUS ID
  '''
  global debug
  if debug:
    print('unary')
    print(p.stack)
    print('\n')    

def p_variables(p):
  '''variables   : id COMMA variables
                 | id
                 '''
  if (len(p) == 2):
      p[0] = [p[1]]
  else:
      p[0] = p[len(p)-1] + [p[1]]
  global debug
  if debug:
    print('variables')
    print(p.stack)
    print('\n')


def p_id(p):
  '''id : ID
        | ID vector
        | ID vector vector
  ''' 
  p[0] = p[1]

def p_vector(p):
  '''vector : LBRACKET integer RBRACKET
            | LBRACKET ID RBRACKET  
            | LBRACKET empty RBRACKET
  ''' 

def p_function_call(p):
  'function_call : ID LPAREN RPAREN'
  global debug
  if debug:
    print('function_call')
    print(p.stack)
    print('\n')

def p_if_sentence(p):
  '''if_sentence : IF LPAREN expression RPAREN function_block empty
                 | IF LPAREN expression RPAREN function_block ELSE function_block
  '''
  global debug
  if debug:
    print('if_sentence')
    print(p.stack)
    print('\n')

def p_while_sentence(p):
  'while_sentence : WHILE LPAREN expression RPAREN function_block'
  global debug
  if debug:
    print('while_sentence')
    print(p.stack)
    print('\n')

def p_do_while_sentence(p):
  'do_while_sentence :  DO function_block WHILE LPAREN expression RPAREN SEMICOLON'
  global debug
  if debug:
    print('do_while_sentence')
    print(p.stack)
    print('\n')

def p_for_sentence(p):
  'for_sentence : FOR LPAREN for_expression RPAREN function_block'
  global debug
  if debug:
    print('for_sentence')
    print(p.stack)
    print('\n')

def p_for_expression(p):
  '''for_expression : declaration SEMICOLON expression SEMICOLON assignation
                    | declaration SEMICOLON expression SEMICOLON unary_operation'''
  global debug
  if debug:
    print('p_for_expression')
    print(p.stack)
    print('\n')

def p_expression(p):
  '''expression : simple_expression
                | expression LESS_THAN simple_expression   
                | expression LESS_OR_EQUAL_THAN simple_expression   
                | expression EQUAL_THAN simple_expression   
                | expression DIFFERENT_THAN simple_expression   
                | expression GREATER_THAN simple_expression   
                | expression GREATER_OR_EQUAL_THAN simple_expression'''
  global debug
  if debug:
    print('p_expression')
    print(p.stack)
    print('\n')

def p_simple_expression(p):
  '''simple_expression : term
                       | PLUS term
                       | MINUS term
                       | simple_expression OR expression_action_2 term
                       | simple_expression PLUS expression_action_2 term
                       | simple_expression MINUS expression_action_2 term'''
  global debug
  if debug:
    print('p_simple_expression')
    print(p.stack)
    print('\n')

def p_term(p):
  '''term : factor
          | term TIMES expression_action_3 factor
          | term DIVIDE expression_action_3 factor
          | term MOD expression_action_3 factor
          | term AND expression_action_3 factor'''
  global debug
  if debug:
    print('p_term')
    print(p.stack)
    print('\n')

def p_factor(p):
  '''factor : id expression_action_1
            | number expression_action_1
            | NOT id expression_action_1
            | LPAREN expression RPAREN'''
  global debug
  if debug:
    print('p_factor')
    print(p.stack)
    print('\n')

def p_number(p):
  '''number : real
            | integer'''
  p[0] = int(p[1])
  global debug
  if debug:
    print('p_number')
    print(p.stack)
    print('\n')

def p_real(p):
  'real : NUMBER DOT NUMBER'
  p[0] = float(''.join([1], p[2], p[3]))
  global debug
  if debug:
    print('p_real')
    print(p.stack)
    print('\n')

def p_integer(p):
  'integer : NUMBER'
  p[0] = int(p[1])
  global debug
  if debug:
    print('p_integer')
    print(p.stack)
    print('\n')

def p_empty(p):
  'empty :'
  global debug
  if debug:
    print('p_empty')
    print(p.stack)
    print('\n')
  pass

# Error rule for syntax errors
def p_error(p):
  print("Syntax error in input!")
  print(p)

def p_expression_action_1(p):
  'expression_action_1 :'
  global operands_stack
  print('action 1')
  print(p[-1])
  operands_stack.append(p[-1])

def p_expression_action_2(p):
  'expression_action_2 :'
  global operands_stack
  print('action 2')
  print(p[-1])
  operators_stack.append(p[-1])

def p_expression_action_3(p):
  'expression_action_3 :'
  global operands_stack
  print('action 3')
  print(p[-1])
  operators_stack.append(p[-1])
 
# Build the parser
global debug
debug = False
parser = yacc.yacc()
 

s = file('pruebas.eskr', 'r').read()
result = parser.parse(s)
# print(result)
# print(symbols_table)
