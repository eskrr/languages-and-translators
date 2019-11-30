 # Yacc example
 
import ply.yacc as yacc
import numpy as np
# Get the token map from the lexer.  This is required.
from eskr_lex import tokens
from symbol import Symbol
from executer import Executer

start = 'program'

global symbols_table
global functions_table
global operands_stack
global operands_stack
global jumps_stack
global quadruples
global term_operators
global factor_operators
global relation_operators
global temporal_count
global dimensions_queue

dimensions_queue = []
operators_stack = []
operands_stack = []
functions_table = {}
symbols_table = {}
jumps_stack = []
quadruples = [['goto', None]]
term_operators = {'+', '||', '-'}
factor_operators = {'*', '/', '&&', '%'}
relation_operators = {'<', '<=', '==', '!=', '>', '>='}
temporal_count = 0

def p_program(p):
  'program : program_block'

def p_program_block(p):
  '''program_block : declaration SEMICOLON program_block 
                   | assignation SEMICOLON program_block
                   | normal_function program_block
                   | main_function'''

def p_normal_function(p):
  'normal_function : FUNCTION ID start_function_action LPAREN RPAREN function_block end_function_action'

def p_main_function(p):
  'main_function : FUNCTION MAIN start_main_function_action LPAREN RPAREN function_block'

def p_start_function_action(p):
  'start_function_action : '
  global functions_table, quadruples
  functions_table[p[-1]] = len(quadruples)

def p_start_main_function_action(p):
  'start_main_function_action : '
  global quadruples
  quadruples[0][1] = len(quadruples)

def p_end_function_action(p):
  'end_function_action : '
  global quadruples
  quadruples.append(['return'])

def p_function_block(p):
  'function_block : LBRACE instruction RBRACE'

def p_instruction(p):
  '''instruction : proposition instruction
                 | empty'''

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

def p_print(p):
  '''print : COUT output_expression
     output_expression : OUTSTREAM expression print_action output_expression
                       | OUTSTREAM expression print_action
                       | OUTSTREAM TEXT print_action output_expression
                       | OUTSTREAM TEXT print_action
                       | OUTSTREAM ENDL print_action output_expression
                       | OUTSTREAM ENDL print_action
  '''

def p_print_action(p):
  'print_action :'
  global quadruples
  global operands_stack
  if p[-1]:
    if p[-1] == 'endl':
      quadruples.append(('print', '\n'))
    else:
      quadruples.append(('print', p[-1]))
  else:
    quadruples.append(('print', operands_stack.pop()))

def p_input(p):
  '''input : CIN input_expression 
     input_expression : INSTREAM id input_action input_expression
                      | INSTREAM id input_action  
  '''

def p_input_action(p):
  'input_action :'
  global quadruples
  global operands_stack
  if p[-1]:
    quadruples.append(('input', p[-1]))

def p_declaration(p):
  'declaration : type variables' 
  global symbols_table
  global dimensions_queue
  for symbol in p[2]: 
    if symbol not in symbols_table:
      symbols_table[symbol] = Symbol(symbol, p[1])
    else:
      print('Variable redeclaration')
      raise SyntaxError('Variable redeclaration')
  while (len(dimensions_queue)):
    print('SIMBOLO: ', symbol)
    symbol = dimensions_queue.pop(0).replace('#', '')
    rows = dimensions_queue.pop(0)
    if len(dimensions_queue) and isinstance(dimensions_queue[0], int):
      cols = dimensions_queue.pop(0)
      symbols_table[symbol].value = np.empty((rows, cols), symbols_table[symbol].type)
    else:
      symbols_table[symbol].value = np.empty(rows, symbols_table[symbol].type)

def p_type(p):
  '''type : INT
          | FLOAT'''
  p[0] = p[1]

def p_assignation(p):
  'assignation : id assignation_action_1 EQUAL assignation_action_2 expression_1 assignation_action_3'

def p_assignation_action_1(p):
  'assignation_action_1 :'
  global operands_stack, symbols_table, dimensions_queue
  print('ASIGNACIONOOOO')
  if p[-1] in symbols_table:
    if len(dimensions_queue) and p[-1] == dimensions_queue[0].replace('#', ''):
      dimensions_queue.pop(0)
      row = dimensions_queue.pop(0)
      if len(dimensions_queue) and isinstance(dimensions_queue[0], int):
        col = dimensions_queue.pop(0)
        operands_stack.append('{}/{}/{}'.format(p[-1], row, col))
      elif len(dimensions_queue) and '##' not in dimensions_queue[0]:
        col = dimensions_queue.pop(0)
        operands_stack.append('{}/{}/{}'.format(p[-1], row, col))
      else:
        operands_stack.append('{}/{}'.format(p[-1],row))
    else:  
      operands_stack.append(p[-1])
  else  :
    print('Variable not declared ' + p[-1])
    raise SyntaxError('Variable not declared ' + p[-1])

def p_assignation_action_2(p):
  'assignation_action_2 :'
  global operators_stack
  operators_stack.append(p[-1])

def p_assignation_action_3(p):
  'assignation_action_3 :'
  global operands_stack, operators_stack, quadruples
  value = operands_stack.pop()
  variable = operands_stack.pop()
  quadruples.append((operators_stack.pop(), value, variable))

def p_unary_operation(p):
  '''unary_operation : ID PLUS PLUS
                     | ID MINUS MINUS
                     | PLUS PLUS ID
                     | MINUS MINUS ID
  '''
  global quadruples
  quadruples.append((p[2], p[1], 1, p[1])) 

def p_variables(p):
  '''variables   : id COMMA variables
                 | id
                 '''
  if (len(p) == 2):
      p[0] = [p[1]]
  else:
      p[0] = p[len(p)-1] + [p[1]]

def p_id(p):
  '''id : ID
        | ID mark_vector vector
        | ID mark_vector vector vector'''
  p[0] = p[1]

def p_mark_vector(p):
  'mark_vector :'
  global dimensions_queue
  dimensions_queue.append('##' + p[-1])

def p_vector(p):
  '''vector : LBRACKET integer vector_action RBRACKET
     vector : LBRACKET ID vector_action RBRACKET
  '''

def p_vector_action(p):
  'vector_action :'
  global dimensions_queue
  dimensions_queue.append(p[-1])

def p_function_call(p):
  'function_call : ID function_call_action LPAREN RPAREN'

def p_function_call_action(p):
  'function_call_action :'
  global quadruples, functions_table
  quadruples.append(('gosub', functions_table[p[-1]]))


def p_if_sentence(p):
  '''if_sentence : IF LPAREN expression_1 RPAREN if_action_1 function_block empty if_action_2
                 | IF LPAREN expression_1 RPAREN if_action_1 function_block ELSE if_action_2 function_block if_action_3
  '''

def p_if_action_1(p):
  'if_action_1 :'
  global operands_stack, jumps_stack, quadruples
  jumps_stack.append(len(quadruples))
  quadruples.append(['gotofalso', operands_stack.pop(), None])

def p_if_action_2(p):
  'if_action_2 : '
  global jumps_stack, quadruples
  if p[-1] == 'else':
    quadruples.append(['goto', None])
  if len(jumps_stack):
    quadruples[jumps_stack.pop()][2] = len(quadruples)
    if p[-1] == 'else':
      jumps_stack.append(len(quadruples) - 1)

def p_if_action_3(p):
  'if_action_3 :'
  global jumps_stack, quadruples
  if len(jumps_stack):
    quadruples[jumps_stack.pop()][1] = len(quadruples)

def p_while_sentence(p):
  'while_sentence : WHILE while_action_1 LPAREN expression_1 RPAREN while_action_2 function_block while_action_3'

def p_while_action_1(p):
  'while_action_1 : '
  global jumps_stack, quadruples
  jumps_stack.append(len(quadruples))

def p_while_action_2(p):
  'while_action_2 : '
  global quadruples, jumps_stack, operands_stack
  jumps_stack.append(len(quadruples))
  quadruples.append(['gotofalso', operands_stack.pop(), None])

def p_while_action_3(p):
  'while_action_3 : '
  global quadruples, jumps_stack
  jump = jumps_stack.pop()
  quadruples.append(('goto', jumps_stack.pop()))
  quadruples[jump][2] = len(quadruples)

def p_do_while_sentence(p):
  'do_while_sentence :  DO do_while_action_1 function_block WHILE LPAREN expression_1 RPAREN do_while_action_2 SEMICOLON'

def p_do_while_action_1(p):
  'do_while_action_1 : '
  global jumps_stack, quadruples
  jumps_stack.append(len(quadruples))

def p_do_while_action_2(p):
  'do_while_action_2 : '
  global jumps_stack, quadruples, operands_stack
  quadruples.append(('gototrue', operands_stack.pop(), jumps_stack.pop()))

def p_for_sentence(p):
  'for_sentence : FOR LPAREN for_expression RPAREN function_block for_action_4'

def p_for_expression(p):
  '''for_expression : assignation for_action_1 SEMICOLON expression_1 for_action_2 SEMICOLON assignation for_action_3
                    | assignation for_action_1 SEMICOLON expression_1 for_action_2 SEMICOLON unary_operation for_action_3'''

def p_for_action_1(p):
  'for_action_1 :'
  global jumps_stack, quadruples
  jumps_stack.append(len(quadruples))

def p_for_action_2(p):
  'for_action_2 :'
  global jumps_stack, quadruples, operands_stack
  quadruples.append(['gotofalso', operands_stack.pop(), None])
  quadruples.append(['goto', None])
  condition_jump = jumps_stack.pop()
  jumps_stack.append(len(quadruples) - 2)
  jumps_stack.append(len(quadruples))
  jumps_stack.append(len(quadruples) - 1)
  jumps_stack.append(condition_jump)
  print(jumps_stack)

def p_for_action_3(p):
  'for_action_3 :'
  global jumps_stack, quadruples
  quadruples.append(('goto', jumps_stack.pop()))
  quadruples[jumps_stack.pop()][1] = len(quadruples)

def p_for_action_4(p):
  'for_action_4 :'
  global jumps_stack, quadruples
  quadruples.append(('goto', jumps_stack.pop()))
  quadruples[jumps_stack.pop()][2] = len(quadruples)

def p_expression_1(p):
  '''expression_1 : expression
                  | expression AND expression_action_3 expression expression_action_5   '''

def p_expression(p):
  '''expression : simple_expression
                | expression LESS_THAN expression_action_8 simple_expression expression_action_9   
                | expression LESS_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9   
                | expression EQUAL_THAN expression_action_8 simple_expression expression_action_9   
                | expression DIFFERENT_THAN expression_action_8 simple_expression expression_action_9   
                | expression GREATER_THAN expression_action_8 simple_expression expression_action_9   
                | expression GREATER_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9'''

def p_simple_expression(p):
  '''simple_expression : term expression_action_4
                       | PLUS term expression_action_4
                       | MINUS term expression_action_4
                       | simple_expression OR expression_action_2 term expression_action_4
                       | simple_expression PLUS expression_action_2 term expression_action_4
                       | simple_expression MINUS expression_action_2 term expression_action_4'''

def p_term(p):
  '''term : factor
          | term TIMES expression_action_3 factor expression_action_5
          | term DIVIDE expression_action_3 factor expression_action_5
          | term MOD expression_action_3 factor expression_action_5'''
  if len(p) == 2:
    p[0] = p[1]

def p_factor(p):
  '''factor : id expression_action_1
            | number expression_action_1
            | NOT id expression_action_1
            | expression_action_6 LPAREN expression RPAREN expression_action_7'''
  if p[1] != '(':
    if len(p) == 4:
      p[0] = p[2]
    else:
      p[0] = p[1]

def p_number(p):
  '''number : real
            | integer'''
  p[0] = int(p[1])

def p_real(p):
  'real : NUMBER DOT NUMBER'
  p[0] = float(''.join( [str(a) for a in p[1:len(p)]] ))

def p_integer(p):
  'integer : NUMBER'
  p[0] = int(p[1])

def p_empty(p):
  'empty :'
  pass

# Error rule for syntax errors
def p_error(p):
  print("Syntax error in input!")
  print(p)

def p_expression_action_1(p):
  'expression_action_1 :'
  global operands_stack, dimensions_queue
  if len(dimensions_queue) and isinstance(p[-1], str) and p[-1] == dimensions_queue[0].replace('#', ''):
    dimensions_queue.pop(0)
    row = dimensions_queue.pop(0)
    if len(dimensions_queue) and isinstance(dimensions_queue[0], int):
      col = dimensions_queue.pop(0)
      operands_stack.append('{}/{}/{}'.format(p[-1], row, col))
    elif len(dimensions_queue) and '##' not in dimensions_queue[0]:
      col = dimensions_queue.pop(0)
      operands_stack.append('{}/{}/{}'.format(p[-1], row, col))
    else:
      operands_stack.append('{}/{}'.format(p[-1],row))
  else:
    operands_stack.append(p[-1])

def p_expression_action_2(p):
  'expression_action_2 :'
  global operators_stack
  operators_stack.append(p[-1])

def p_expression_action_3(p):
  'expression_action_3 :'
  global operators_stack
  operators_stack.append(p[-1])

def p_expression_action_4(p):
  'expression_action_4 :'
  global operands_stack, operators_stack, temporal_count, term_operators, quadruples
  if len(operators_stack) and operators_stack[-1] in term_operators:
      operand_2 = operands_stack.pop()
      operand_1 = operands_stack.pop()
      temporal = '#' + str(temporal_count)
      temporal_count = temporal_count + 1
      quadruples.append((operators_stack.pop(), operand_1, operand_2, temporal))
      operands_stack.append(temporal)

def p_expression_action_5(p):
  'expression_action_5 :'
  global operands_stack, operators_stack, temporal_count, factor_operators, quadruples
  if len(operators_stack) and operators_stack[-1] in factor_operators:
      operand_2 = operands_stack.pop()
      operand_1 = operands_stack.pop()
      temporal = '#' + str(temporal_count)
      temporal_count = temporal_count + 1
      quadruples.append((operators_stack.pop(), operand_1, operand_2, temporal))
      operands_stack.append(temporal)

def p_expression_action_6(p):
  'expression_action_6 :'
  global operators_stack
  operators_stack.append(None)

def p_expression_action_7(p):
  'expression_action_7 :'
  global operators_stack
  operators_stack.pop()

def p_expression_action_8(p):
  'expression_action_8 :'
  global operators_stack
  operators_stack.append(p[-1])

def p_expression_action_9(p):
  'expression_action_9 :'
  global operands_stack, operators_stack, temporal_count, relation_operators, quadruples
  if len(operators_stack) and operators_stack[-1] in relation_operators:
      operand_2 = operands_stack.pop()
      operand_1 = operands_stack.pop()
      temporal = '#' + str(temporal_count)
      temporal_count = temporal_count + 1
      quadruples.append((operators_stack.pop(), operand_1, operand_2, temporal))
      operands_stack.append(temporal)
 
# Build the parser
parser = yacc.yacc()

s = file('multiply.eskr', 'r').read()
result = parser.parse(s)
for i in range(len(quadruples)):
  print(i, quadruples[i])

executer = Executer(quadruples, symbols_table, temporal_count)
executer.execute()
