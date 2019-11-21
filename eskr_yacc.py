 # Yacc example
 
import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from eskr_lex import tokens

start = 'program'
symbols_table = {}
operands_stack = []
operators_stack = []
jumps_stack = []
quadruples = []
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
  'normal_function : FUNCTION ID LPAREN RPAREN function_block'

def p_main_function(p):
  'main_function : FUNCTION MAIN LPAREN RPAREN function_block'

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
  'declaration : type variables' 
  global symbols_table  
  for symbol in p[2]: 
    if symbol not in symbols_table: 
      symbols_table[symbol] = p[1]  
    else:
      print('Variable redeclaration')
      raise SyntaxError('Variable redeclaration')

def p_type(p):
  '''type : INT
          | DOUBLE'''
  p[0] = p[1]

def p_assignation(p):
  'assignation : id assignation_action_1 EQUAL assignation_action_2 expression assignation_action_3'

def p_assignation_action_1(p):
  'assignation_action_1 :'
  global operands_stack
  if p[-1] in symbols_table:
    operands_stack.append(p[-1])
  else:
    print('Variable not declared ' + p[-1])
    raise SyntaxError('Variable not declared ' + p[-1])


def p_assignation_action_2(p):
  'assignation_action_2 :'
  global operators_stack
  operators_stack.append(p[-1])

def p_assignation_action_3(p):
  'assignation_action_3 :'
  global operands_stack
  global operators_stack
  global quadruples
  value = operands_stack.pop()
  variable = operands_stack.pop()
  quadruples.append((operators_stack.pop(), value, None, variable))

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

def p_if_sentence(p):
  '''if_sentence : IF LPAREN expression RPAREN if_action_1 function_block empty if_action_2
                 | IF LPAREN expression RPAREN if_action_1 function_block ELSE if_action_2 function_block if_action_3
  '''

def p_if_action_1(p):
  'if_action_1 :'
  global operands_stack
  global jumps_stack
  global quadruples
  jumps_stack.append(len(quadruples))
  quadruples.append(['gotofalso', operands_stack.pop(), None])

def p_if_action_2(p):
  'if_action_2 : '
  global operands_stack
  global jumps_stack
  global quadruples
  if p[-1] == 'else':
    quadruples.append(['goto', None])
  if len(jumps_stack):
    quadruples[jumps_stack.pop()][2] = len(quadruples)
    if p[-1] == 'else':
      jumps_stack.append(len(quadruples) - 1)

def p_if_action_3(p):
  'if_action_3 :'
  global operands_stack
  global jumps_stack
  global quadruples
  if len(jumps_stack):
    quadruples[jumps_stack.pop()][1] = len(quadruples)

def p_while_sentence(p):
  'while_sentence : WHILE while_action_1 LPAREN expression RPAREN while_action_2 function_block while_action_3'

def p_while_action_1(p):
  'while_action_1 : '
  global jumps_stack
  global quadruples
  jumps_stack.append(len(quadruples))

def p_while_action_2(p):
  'while_action_2 : '
  global quadruples
  global jumps_stack
  global operands_stack
  jumps_stack.append(len(quadruples))
  quadruples.append(['gotofalso', operands_stack.pop(), None])

def p_while_action_3(p):
  'while_action_3 : '
  global quadruples
  global jumps_stack
  jump = jumps_stack.pop()
  quadruples.append(('goto', jumps_stack.pop()))
  quadruples[jump][2] = len(quadruples)

def p_do_while_sentence(p):
  'do_while_sentence :  DO do_while_action_1 function_block WHILE LPAREN expression RPAREN do_while_action_2 SEMICOLON'

def p_do_while_action_1(p):
  'do_while_action_1 : '
  global jumps_stack
  global quadruples
  jumps_stack.append(len(quadruples))

def p_do_while_action_2(p):
  'do_while_action_2 : '
  global jumps_stack
  global quadruples
  global operands_stack
  quadruples.append(('gototrue', operands_stack.pop(), jumps_stack.pop()))

def p_for_sentence(p):
  'for_sentence : FOR LPAREN for_expression RPAREN function_block for_action_4'

def p_for_expression(p):
  '''for_expression : assignation for_action_1 SEMICOLON expression for_action_2 SEMICOLON assignation for_action_3
                    | assignation for_action_1 SEMICOLON expression for_action_2 SEMICOLON unary_operation for_action_3'''

def p_for_action_1(p):
  'for_action_1 :'
  global jumps_stack
  global quadruples
  jumps_stack.append(len(quadruples))

def p_for_action_2(p):
  'for_action_2 :'
  global jumps_stack
  global quadruples
  global operands_stack
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
  global jumps_stack
  global quadruples
  quadruples.append(('goto', jumps_stack.pop()))
  quadruples[jumps_stack.pop()][1] = len(quadruples)

def p_for_action_4(p):
  'for_action_4 :'
  global jumps_stack
  global quadruples
  quadruples.append(('goto', jumps_stack.pop()))
  quadruples[jumps_stack.pop()][2] = len(quadruples)

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
          | term MOD expression_action_3 factor expression_action_5
          | term AND expression_action_3 factor expression_action_5'''
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
  p[0] = float(''.join([1], p[2], p[3]))

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
  global operands_stack
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
  global operands_stack
  global operators_stack
  global temporal_count
  if len(operators_stack) and operators_stack[-1] in term_operators:
      operand_2 = operands_stack.pop()
      operand_1 = operands_stack.pop()
      temporal = 'T' + str(temporal_count)
      temporal_count = temporal_count + 1
      quadruples.append((operators_stack.pop(), operand_1, operand_2, temporal))
      operands_stack.append(temporal)

def p_expression_action_5(p):
  'expression_action_5 :'
  global operands_stack
  global operators_stack
  global temporal_count
  if len(operators_stack) and operators_stack[-1] in factor_operators:
      operand_2 = operands_stack.pop()
      operand_1 = operands_stack.pop()
      temporal = 'T' + str(temporal_count)
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
  global operands_stack
  global operators_stack
  global temporal_count
  if len(operators_stack) and operators_stack[-1] in relation_operators:
      operand_2 = operands_stack.pop()
      operand_1 = operands_stack.pop()
      temporal = 'T' + str(temporal_count)
      temporal_count = temporal_count + 1
      quadruples.append((operators_stack.pop(), operand_1, operand_2, temporal))
      operands_stack.append(temporal)
 
# Build the parser
parser = yacc.yacc()
 

s = file('pruebas.eskr', 'r').read()
result = parser.parse(s)
# print(result)
# print(symbols_table)
# print(quadruples)
for i in range(len(quadruples)):
  print(i, quadruples[i])
