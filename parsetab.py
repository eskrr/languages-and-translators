
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND CIN COMMA COUT DIFFERENT_THAN DIVIDE DO DOT ELSE EQUAL EQUAL_THAN FLOAT FOR FUNCTION GREATER_OR_EQUAL_THAN GREATER_THAN ID IF INSTREAM INT LBRACE LBRACKET LESS_OR_EQUAL_THAN LESS_THAN LPAREN MAIN MINUS MOD NOT NUMBER OR OUTSTREAM PLUS RBRACE RBRACKET RPAREN SEMICOLON TEXT TIMES WHILEprogram : program_blockprogram_block : declaration SEMICOLON program_block \n                   | assignation SEMICOLON program_block\n                   | normal_function program_block\n                   | main_functionnormal_function : FUNCTION ID start_function_action LPAREN RPAREN function_block end_function_actionmain_function : FUNCTION MAIN start_main_function_action LPAREN RPAREN function_blockstart_function_action : start_main_function_action : end_function_action : function_block : LBRACE instruction RBRACEinstruction : proposition instruction\n                 | emptyproposition : function_call SEMICOLON\n                 | assignation SEMICOLON\n                 | print SEMICOLON\n                 | input SEMICOLON\n                 | unary_operation SEMICOLON\n                 | if_sentence\n                 | while_sentence\n                 | do_while_sentence\n                 | for_sentenceprint : COUT output_expression\n     output_expression : OUTSTREAM expression print_action output_expression\n                       | OUTSTREAM expression print_action\n                       | OUTSTREAM TEXT print_action output_expression\n                       | OUTSTREAM TEXT print_action\n  print_action :input : CIN input_expression \n     input_expression : INSTREAM id input_action input_expression\n                      | INSTREAM id input_action  \n  input_action :declaration : type variablestype : INT\n          | FLOATassignation : id assignation_action_1 EQUAL assignation_action_2 expression assignation_action_3assignation_action_1 :assignation_action_2 :assignation_action_3 :unary_operation : ID PLUS PLUS\n                     | ID MINUS MINUS\n                     | PLUS PLUS ID\n                     | MINUS MINUS ID\n  variables   : id COMMA variables\n                 | id\n                 id : ID\n        | ID vector\n        | ID vector vector\n  vector : LBRACKET integer RBRACKET\n            | LBRACKET ID RBRACKET  \n            | LBRACKET empty RBRACKET\n  function_call : ID function_call_action LPAREN RPARENfunction_call_action :if_sentence : IF LPAREN expression RPAREN if_action_1 function_block empty if_action_2\n                 | IF LPAREN expression RPAREN if_action_1 function_block ELSE if_action_2 function_block if_action_3\n  if_action_1 :if_action_2 : if_action_3 :while_sentence : WHILE while_action_1 LPAREN expression RPAREN while_action_2 function_block while_action_3while_action_1 : while_action_2 : while_action_3 : do_while_sentence :  DO do_while_action_1 function_block WHILE LPAREN expression RPAREN do_while_action_2 SEMICOLONdo_while_action_1 : do_while_action_2 : for_sentence : FOR LPAREN for_expression RPAREN function_block for_action_4for_expression : assignation for_action_1 SEMICOLON expression for_action_2 SEMICOLON assignation for_action_3\n                    | assignation for_action_1 SEMICOLON expression for_action_2 SEMICOLON unary_operation for_action_3for_action_1 :for_action_2 :for_action_3 :for_action_4 :expression : simple_expression\n                | expression LESS_THAN expression_action_8 simple_expression expression_action_9   \n                | expression LESS_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9   \n                | expression EQUAL_THAN expression_action_8 simple_expression expression_action_9   \n                | expression DIFFERENT_THAN expression_action_8 simple_expression expression_action_9   \n                | expression GREATER_THAN expression_action_8 simple_expression expression_action_9   \n                | expression GREATER_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9simple_expression : term expression_action_4\n                       | PLUS term expression_action_4\n                       | MINUS term expression_action_4\n                       | simple_expression OR expression_action_2 term expression_action_4\n                       | simple_expression PLUS expression_action_2 term expression_action_4\n                       | simple_expression MINUS expression_action_2 term expression_action_4term : factor\n          | term TIMES expression_action_3 factor expression_action_5\n          | term DIVIDE expression_action_3 factor expression_action_5\n          | term MOD expression_action_3 factor expression_action_5\n          | term AND expression_action_3 factor expression_action_5factor : id expression_action_1\n            | number expression_action_1\n            | NOT id expression_action_1\n            | expression_action_6 LPAREN expression RPAREN expression_action_7number : real\n            | integerreal : NUMBER DOT NUMBERinteger : NUMBERempty :expression_action_1 :expression_action_2 :expression_action_3 :expression_action_4 :expression_action_5 :expression_action_6 :expression_action_7 :expression_action_8 :expression_action_9 :'
    
_lr_action_items = {'DO':([78,101,104,105,107,119,138,143,144,145,153,154,196,202,203,205,208,210,213,214,218,221,],[99,-21,99,-20,-22,-19,-14,-16,-17,-18,-15,-11,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'COUT':([78,101,104,105,107,119,138,143,144,145,153,154,196,202,203,205,208,210,213,214,218,221,],[100,-21,100,-20,-22,-19,-14,-16,-17,-18,-15,-11,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'CIN':([78,101,104,105,107,119,138,143,144,145,153,154,196,202,203,205,208,210,213,214,218,221,],[114,-21,114,-20,-22,-19,-14,-16,-17,-18,-15,-11,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'TEXT':([136,],[170,]),'EQUAL':([2,8,13,20,32,38,39,40,115,217,],[-37,-46,23,-47,-48,-49,-50,-51,-46,-46,]),'LBRACKET':([8,20,38,39,40,115,217,],[19,19,-49,-50,-51,19,19,]),'WHILE':([78,101,104,105,107,119,138,143,144,145,153,154,169,196,202,203,205,208,210,213,214,218,221,],[103,-21,103,-20,-22,-19,-14,-16,-17,-18,-15,-11,182,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'DIFFERENT_THAN':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,181,185,199,201,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,74,-103,-92,-91,-103,-80,-100,-82,-81,-97,74,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,74,74,74,74,74,]),'LESS_THAN':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,181,185,199,201,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,76,-103,-92,-91,-103,-80,-100,-82,-81,-97,76,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,76,76,76,76,76,]),'MINUS':([8,20,23,32,34,38,39,40,41,43,44,46,47,48,49,51,56,57,58,59,64,68,70,71,73,74,75,76,77,78,81,82,86,92,93,94,95,96,97,98,101,104,105,106,107,115,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,138,143,144,145,151,152,153,154,155,156,157,158,159,160,161,162,172,191,195,196,202,203,205,208,210,211,213,214,217,218,221,],[-46,-47,-38,-48,42,-49,-50,-51,-96,-100,-100,-86,-95,60,-98,-103,-103,-92,-91,-103,42,-80,-107,-107,-107,-107,-107,-107,-100,106,-82,-81,-97,42,42,42,42,42,42,-93,-21,106,-20,141,-22,151,-19,-103,-103,-103,-106,-104,-104,-104,-104,60,60,60,60,60,60,42,-14,-16,-17,-18,180,42,-15,-11,-85,-84,-83,-94,-90,-88,-87,-89,42,42,42,-72,-66,-99,-62,-57,-59,106,-54,-63,151,-58,-55,]),'DOT':([49,],[63,]),'RBRACE':([78,101,104,105,107,112,118,119,138,140,143,144,145,153,154,196,202,203,205,208,210,213,214,218,221,],[-99,-21,-99,-20,-22,-13,154,-19,-14,-12,-16,-17,-18,-15,-11,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'RPAREN':([8,20,32,36,37,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,72,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,173,174,176,178,179,180,181,185,199,215,216,219,220,],[-46,-47,-48,54,55,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,-39,-103,-92,-91,-103,-80,-36,-100,-82,-81,-97,124,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,-43,-42,187,-40,189,-41,190,194,204,-71,-71,-67,-68,]),'SEMICOLON':([7,8,9,14,15,20,32,35,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,72,77,81,82,86,98,102,109,110,111,117,121,122,123,124,125,126,127,128,129,130,131,132,133,134,137,148,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,173,174,175,177,178,180,183,184,186,188,189,192,193,197,201,204,206,209,],[18,-46,21,-33,-45,-47,-48,-44,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,-39,-103,-92,-91,-103,-80,-36,-100,-82,-81,-97,-93,138,143,144,145,153,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-23,-29,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,-28,-28,-43,-42,-69,-32,-40,-41,-27,-25,195,-31,-52,-26,-24,-30,-70,-65,211,214,]),'PLUS':([8,20,23,32,34,38,39,40,41,43,44,46,47,48,49,51,56,57,58,59,64,68,70,71,73,74,75,76,77,78,81,82,86,92,93,94,95,96,97,98,101,104,105,107,108,115,119,121,122,123,124,125,126,127,128,129,130,131,132,133,134,136,138,143,144,145,149,152,153,154,155,156,157,158,159,160,161,162,172,191,195,196,202,203,205,208,210,211,213,214,217,218,221,],[-46,-47,-38,-48,45,-49,-50,-51,-96,-100,-100,-86,-95,61,-98,-103,-103,-92,-91,-103,45,-80,-107,-107,-107,-107,-107,-107,-100,108,-82,-81,-97,45,45,45,45,45,45,-93,-21,108,-20,-22,142,149,-19,-103,-103,-103,-106,-104,-104,-104,-104,61,61,61,61,61,61,45,-14,-16,-17,-18,178,45,-15,-11,-85,-84,-83,-94,-90,-88,-87,-89,45,45,45,-72,-66,-99,-62,-57,-59,108,-54,-63,149,-58,-55,]),'COMMA':([8,15,20,32,38,39,40,],[-46,24,-47,-48,-49,-50,-51,]),'INSTREAM':([8,20,32,38,39,40,114,177,188,],[-46,-47,-48,-49,-50,-51,147,-32,147,]),'$end':([1,3,4,22,27,33,79,154,],[-5,0,-1,-4,-2,-3,-7,-11,]),'FUNCTION':([0,11,18,21,80,120,154,],[6,6,6,6,-10,-6,-11,]),'DIVIDE':([8,20,32,38,39,40,41,43,44,46,47,49,51,56,57,58,59,77,86,98,121,122,123,124,125,126,127,128,158,159,160,161,162,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-98,66,66,-92,-91,66,-100,-97,-93,66,66,66,-106,-104,-104,-104,-104,-94,-90,-88,-87,-89,]),'FOR':([78,101,104,105,107,119,138,143,144,145,153,154,196,202,203,205,208,210,213,214,218,221,],[113,-21,113,-20,-22,-19,-14,-16,-17,-18,-15,-11,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'NUMBER':([19,23,34,42,45,60,61,62,63,64,65,66,67,69,70,71,73,74,75,76,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[28,-38,49,49,49,-101,-101,-101,86,49,-102,-102,-102,-102,-107,-107,-107,-107,-107,-107,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'OUTSTREAM':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,56,57,58,59,68,77,81,82,86,98,100,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,170,171,183,184,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,-103,-92,-91,-103,-80,-100,-82,-81,-97,-93,136,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,-28,-28,136,136,]),'TIMES':([8,20,32,38,39,40,41,43,44,46,47,49,51,56,57,58,59,77,86,98,121,122,123,124,125,126,127,128,158,159,160,161,162,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-98,67,67,-92,-91,67,-100,-97,-93,67,67,67,-106,-104,-104,-104,-104,-94,-90,-88,-87,-89,]),'LPAREN':([16,17,23,25,26,34,42,45,50,60,61,62,64,65,66,67,69,70,71,73,74,75,76,83,84,85,88,89,90,91,92,93,94,95,96,97,103,113,115,116,136,139,150,152,172,182,191,195,],[-9,-8,-38,36,37,-105,-105,-105,64,-101,-101,-101,-105,-102,-102,-102,-102,-107,-107,-107,-107,-107,-107,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-105,-60,146,-53,152,-105,172,179,-105,-105,191,-105,-105,]),'GREATER_THAN':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,181,185,199,201,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,73,-103,-92,-91,-103,-80,-100,-82,-81,-97,73,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,73,73,73,73,73,]),'ELSE':([154,203,],[-11,207,]),'ID':([0,5,6,10,11,12,18,19,21,23,24,34,42,45,53,60,61,62,64,65,66,67,69,70,71,73,74,75,76,78,80,83,84,85,88,89,90,91,92,93,94,95,96,97,101,104,105,107,119,120,136,138,141,142,143,144,145,146,147,152,153,154,172,191,195,196,202,203,205,208,210,211,213,214,218,221,],[8,8,17,-34,8,-35,8,30,8,-38,8,8,8,8,8,-101,-101,-101,8,-102,-102,-102,-102,-107,-107,-107,-107,-107,-107,115,-10,8,8,8,8,8,8,8,8,8,8,8,8,8,-21,115,-20,-22,-19,-6,8,-14,173,174,-16,-17,-18,8,8,8,-15,-11,8,8,8,-72,-66,-99,-62,-57,-59,217,-54,-63,-58,-55,]),'IF':([78,101,104,105,107,119,138,143,144,145,153,154,196,202,203,205,208,210,213,214,218,221,],[116,-21,116,-20,-22,-19,-14,-16,-17,-18,-15,-11,-72,-66,-99,-62,-57,-59,-54,-63,-58,-55,]),'AND':([8,20,32,38,39,40,41,43,44,46,47,49,51,56,57,58,59,77,86,98,121,122,123,124,125,126,127,128,158,159,160,161,162,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-98,65,65,-92,-91,65,-100,-97,-93,65,65,65,-106,-104,-104,-104,-104,-94,-90,-88,-87,-89,]),'GREATER_OR_EQUAL_THAN':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,181,185,199,201,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,70,-103,-92,-91,-103,-80,-100,-82,-81,-97,70,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,70,70,70,70,70,]),'LBRACE':([54,55,99,135,187,190,194,198,200,207,212,],[78,78,-64,78,78,-56,-61,78,78,-57,78,]),'EQUAL_THAN':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,181,185,199,201,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,71,-103,-92,-91,-103,-80,-100,-82,-81,-97,71,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,71,71,71,71,71,]),'INT':([0,11,18,21,80,120,154,],[10,10,10,10,-10,-6,-11,]),'FLOAT':([0,11,18,21,80,120,154,],[12,12,12,12,-10,-6,-11,]),'NOT':([23,34,42,45,60,61,62,64,65,66,67,69,70,71,73,74,75,76,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[-38,53,53,53,-101,-101,-101,53,-102,-102,-102,-102,-107,-107,-107,-107,-107,-107,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'RBRACKET':([19,28,29,30,31,],[-99,-98,38,39,40,]),'MAIN':([6,],[16,]),'LESS_OR_EQUAL_THAN':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,52,56,57,58,59,68,77,81,82,86,87,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,163,164,165,166,167,168,171,181,185,199,201,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-73,-98,-103,75,-103,-92,-91,-103,-80,-100,-82,-81,-97,75,-93,-103,-103,-103,-106,-104,-104,-104,-104,-108,-108,-108,-108,-108,-108,-85,-84,-83,-94,-90,-88,-87,-89,-79,-76,-78,-77,-75,-74,75,75,75,75,75,]),'OR':([8,20,32,38,39,40,41,43,44,46,47,48,49,51,56,57,58,59,68,77,81,82,86,98,121,122,123,124,125,126,127,128,129,130,131,132,133,134,155,156,157,158,159,160,161,162,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,62,-98,-103,-103,-92,-91,-103,-80,-100,-82,-81,-97,-93,-103,-103,-103,-106,-104,-104,-104,-104,62,62,62,62,62,62,-85,-84,-83,-94,-90,-88,-87,-89,]),'MOD':([8,20,32,38,39,40,41,43,44,46,47,49,51,56,57,58,59,77,86,98,121,122,123,124,125,126,127,128,158,159,160,161,162,],[-46,-47,-48,-49,-50,-51,-96,-100,-100,-86,-95,-98,69,69,-92,-91,69,-100,-97,-93,69,69,69,-106,-104,-104,-104,-104,-94,-90,-88,-87,-89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main_function':([0,11,18,21,],[1,1,1,1,]),'do_while_sentence':([78,104,],[101,101,]),'assignation_action_2':([23,],[34,]),'assignation_action_3':([52,],[72,]),'variables':([5,24,],[14,35,]),'assignation_action_1':([2,],[13,]),'do_while_action_1':([99,],[135,]),'number':([34,42,45,64,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'function_call':([78,104,],[102,102,]),'proposition':([78,104,],[104,104,]),'do_while_action_2':([204,],[209,]),'if_action_2':([207,208,],[212,213,]),'while_sentence':([78,104,],[105,105,]),'simple_expression':([34,64,92,93,94,95,96,97,136,152,172,191,195,],[48,48,129,130,131,132,133,134,48,48,48,48,48,]),'id':([0,5,11,18,21,24,34,42,45,53,64,78,83,84,85,88,89,90,91,92,93,94,95,96,97,104,136,146,147,152,172,191,195,211,],[2,15,2,2,2,15,44,44,44,77,44,2,44,44,44,44,44,44,44,44,44,44,44,44,44,2,44,2,177,44,44,44,44,2,]),'expression_action_2':([60,61,62,],[83,84,85,]),'end_function_action':([80,],[120,]),'instruction':([78,104,],[118,140,]),'if_action_1':([190,],[198,]),'start_main_function_action':([16,],[25,]),'if_action_3':([218,],[221,]),'program':([0,],[3,]),'factor':([34,42,45,64,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[46,46,46,46,46,46,46,125,126,127,128,46,46,46,46,46,46,46,46,46,46,46,]),'print':([78,104,],[109,109,]),'input':([78,104,],[110,110,]),'type':([0,11,18,21,],[5,5,5,5,]),'empty':([19,78,104,203,],[31,112,112,208,]),'real':([34,42,45,64,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'unary_operation':([78,104,211,],[111,111,216,]),'function_call_action':([115,],[150,]),'input_action':([177,],[188,]),'for_expression':([146,],[176,]),'while_action_3':([205,],[210,]),'program_block':([0,11,18,21,],[4,22,27,33,]),'for_action_1':([175,],[186,]),'while_action_2':([194,],[200,]),'expression_action_5':([125,126,127,128,],[159,160,161,162,]),'start_function_action':([17,],[26,]),'expression_action_7':([124,],[158,]),'expression_action_6':([34,42,45,64,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'expression_action_1':([43,44,77,],[57,58,98,]),'while_action_1':([103,],[139,]),'expression_action_3':([65,66,67,69,],[88,89,90,91,]),'declaration':([0,11,18,21,],[7,7,7,7,]),'function_block':([54,55,135,187,198,200,212,],[79,80,169,196,203,205,218,]),'integer':([19,34,42,45,64,83,84,85,88,89,90,91,92,93,94,95,96,97,136,152,172,191,195,],[29,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'expression_action_9':([129,130,131,132,133,134,],[163,164,165,166,167,168,]),'expression_action_8':([70,71,73,74,75,76,],[92,93,94,95,96,97,]),'for_action_3':([215,216,],[219,220,]),'for_action_2':([201,],[206,]),'term':([34,42,45,64,83,84,85,92,93,94,95,96,97,136,152,172,191,195,],[51,56,59,51,121,122,123,51,51,51,51,51,51,51,51,51,51,51,]),'assignation':([0,11,18,21,78,104,146,211,],[9,9,9,9,117,117,175,215,]),'expression_action_4':([51,56,59,121,122,123,],[68,81,82,155,156,157,]),'if_sentence':([78,104,],[119,119,]),'normal_function':([0,11,18,21,],[11,11,11,11,]),'input_expression':([114,188,],[148,197,]),'output_expression':([100,183,184,],[137,192,193,]),'vector':([8,20,115,217,],[20,32,20,20,]),'print_action':([170,171,],[183,184,]),'expression':([34,64,136,152,172,191,195,],[52,87,171,181,185,199,201,]),'for_sentence':([78,104,],[107,107,]),'for_action_4':([196,],[202,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_block','program',1,'p_program','eskr_yacc.py',34),
  ('program_block -> declaration SEMICOLON program_block','program_block',3,'p_program_block','eskr_yacc.py',37),
  ('program_block -> assignation SEMICOLON program_block','program_block',3,'p_program_block','eskr_yacc.py',38),
  ('program_block -> normal_function program_block','program_block',2,'p_program_block','eskr_yacc.py',39),
  ('program_block -> main_function','program_block',1,'p_program_block','eskr_yacc.py',40),
  ('normal_function -> FUNCTION ID start_function_action LPAREN RPAREN function_block end_function_action','normal_function',7,'p_normal_function','eskr_yacc.py',43),
  ('main_function -> FUNCTION MAIN start_main_function_action LPAREN RPAREN function_block','main_function',6,'p_main_function','eskr_yacc.py',46),
  ('start_function_action -> <empty>','start_function_action',0,'p_start_function_action','eskr_yacc.py',49),
  ('start_main_function_action -> <empty>','start_main_function_action',0,'p_start_main_function_action','eskr_yacc.py',54),
  ('end_function_action -> <empty>','end_function_action',0,'p_end_function_action','eskr_yacc.py',59),
  ('function_block -> LBRACE instruction RBRACE','function_block',3,'p_function_block','eskr_yacc.py',64),
  ('instruction -> proposition instruction','instruction',2,'p_instruction','eskr_yacc.py',67),
  ('instruction -> empty','instruction',1,'p_instruction','eskr_yacc.py',68),
  ('proposition -> function_call SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',71),
  ('proposition -> assignation SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',72),
  ('proposition -> print SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',73),
  ('proposition -> input SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',74),
  ('proposition -> unary_operation SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',75),
  ('proposition -> if_sentence','proposition',1,'p_proposition','eskr_yacc.py',76),
  ('proposition -> while_sentence','proposition',1,'p_proposition','eskr_yacc.py',77),
  ('proposition -> do_while_sentence','proposition',1,'p_proposition','eskr_yacc.py',78),
  ('proposition -> for_sentence','proposition',1,'p_proposition','eskr_yacc.py',79),
  ('print -> COUT output_expression','print',2,'p_print','eskr_yacc.py',82),
  ('output_expression -> OUTSTREAM expression print_action output_expression','output_expression',4,'p_print','eskr_yacc.py',83),
  ('output_expression -> OUTSTREAM expression print_action','output_expression',3,'p_print','eskr_yacc.py',84),
  ('output_expression -> OUTSTREAM TEXT print_action output_expression','output_expression',4,'p_print','eskr_yacc.py',85),
  ('output_expression -> OUTSTREAM TEXT print_action','output_expression',3,'p_print','eskr_yacc.py',86),
  ('print_action -> <empty>','print_action',0,'p_print_action','eskr_yacc.py',90),
  ('input -> CIN input_expression','input',2,'p_input','eskr_yacc.py',99),
  ('input_expression -> INSTREAM id input_action input_expression','input_expression',4,'p_input','eskr_yacc.py',100),
  ('input_expression -> INSTREAM id input_action','input_expression',3,'p_input','eskr_yacc.py',101),
  ('input_action -> <empty>','input_action',0,'p_input_action','eskr_yacc.py',105),
  ('declaration -> type variables','declaration',2,'p_declaration','eskr_yacc.py',112),
  ('type -> INT','type',1,'p_type','eskr_yacc.py',122),
  ('type -> FLOAT','type',1,'p_type','eskr_yacc.py',123),
  ('assignation -> id assignation_action_1 EQUAL assignation_action_2 expression assignation_action_3','assignation',6,'p_assignation','eskr_yacc.py',127),
  ('assignation_action_1 -> <empty>','assignation_action_1',0,'p_assignation_action_1','eskr_yacc.py',130),
  ('assignation_action_2 -> <empty>','assignation_action_2',0,'p_assignation_action_2','eskr_yacc.py',139),
  ('assignation_action_3 -> <empty>','assignation_action_3',0,'p_assignation_action_3','eskr_yacc.py',144),
  ('unary_operation -> ID PLUS PLUS','unary_operation',3,'p_unary_operation','eskr_yacc.py',151),
  ('unary_operation -> ID MINUS MINUS','unary_operation',3,'p_unary_operation','eskr_yacc.py',152),
  ('unary_operation -> PLUS PLUS ID','unary_operation',3,'p_unary_operation','eskr_yacc.py',153),
  ('unary_operation -> MINUS MINUS ID','unary_operation',3,'p_unary_operation','eskr_yacc.py',154),
  ('variables -> id COMMA variables','variables',3,'p_variables','eskr_yacc.py',160),
  ('variables -> id','variables',1,'p_variables','eskr_yacc.py',161),
  ('id -> ID','id',1,'p_id','eskr_yacc.py',169),
  ('id -> ID vector','id',2,'p_id','eskr_yacc.py',170),
  ('id -> ID vector vector','id',3,'p_id','eskr_yacc.py',171),
  ('vector -> LBRACKET integer RBRACKET','vector',3,'p_vector','eskr_yacc.py',176),
  ('vector -> LBRACKET ID RBRACKET','vector',3,'p_vector','eskr_yacc.py',177),
  ('vector -> LBRACKET empty RBRACKET','vector',3,'p_vector','eskr_yacc.py',178),
  ('function_call -> ID function_call_action LPAREN RPAREN','function_call',4,'p_function_call','eskr_yacc.py',182),
  ('function_call_action -> <empty>','function_call_action',0,'p_function_call_action','eskr_yacc.py',185),
  ('if_sentence -> IF LPAREN expression RPAREN if_action_1 function_block empty if_action_2','if_sentence',8,'p_if_sentence','eskr_yacc.py',191),
  ('if_sentence -> IF LPAREN expression RPAREN if_action_1 function_block ELSE if_action_2 function_block if_action_3','if_sentence',10,'p_if_sentence','eskr_yacc.py',192),
  ('if_action_1 -> <empty>','if_action_1',0,'p_if_action_1','eskr_yacc.py',196),
  ('if_action_2 -> <empty>','if_action_2',0,'p_if_action_2','eskr_yacc.py',202),
  ('if_action_3 -> <empty>','if_action_3',0,'p_if_action_3','eskr_yacc.py',212),
  ('while_sentence -> WHILE while_action_1 LPAREN expression RPAREN while_action_2 function_block while_action_3','while_sentence',8,'p_while_sentence','eskr_yacc.py',218),
  ('while_action_1 -> <empty>','while_action_1',0,'p_while_action_1','eskr_yacc.py',221),
  ('while_action_2 -> <empty>','while_action_2',0,'p_while_action_2','eskr_yacc.py',226),
  ('while_action_3 -> <empty>','while_action_3',0,'p_while_action_3','eskr_yacc.py',232),
  ('do_while_sentence -> DO do_while_action_1 function_block WHILE LPAREN expression RPAREN do_while_action_2 SEMICOLON','do_while_sentence',9,'p_do_while_sentence','eskr_yacc.py',239),
  ('do_while_action_1 -> <empty>','do_while_action_1',0,'p_do_while_action_1','eskr_yacc.py',242),
  ('do_while_action_2 -> <empty>','do_while_action_2',0,'p_do_while_action_2','eskr_yacc.py',247),
  ('for_sentence -> FOR LPAREN for_expression RPAREN function_block for_action_4','for_sentence',6,'p_for_sentence','eskr_yacc.py',252),
  ('for_expression -> assignation for_action_1 SEMICOLON expression for_action_2 SEMICOLON assignation for_action_3','for_expression',8,'p_for_expression','eskr_yacc.py',255),
  ('for_expression -> assignation for_action_1 SEMICOLON expression for_action_2 SEMICOLON unary_operation for_action_3','for_expression',8,'p_for_expression','eskr_yacc.py',256),
  ('for_action_1 -> <empty>','for_action_1',0,'p_for_action_1','eskr_yacc.py',259),
  ('for_action_2 -> <empty>','for_action_2',0,'p_for_action_2','eskr_yacc.py',264),
  ('for_action_3 -> <empty>','for_action_3',0,'p_for_action_3','eskr_yacc.py',276),
  ('for_action_4 -> <empty>','for_action_4',0,'p_for_action_4','eskr_yacc.py',282),
  ('expression -> simple_expression','expression',1,'p_expression','eskr_yacc.py',288),
  ('expression -> expression LESS_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',289),
  ('expression -> expression LESS_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',290),
  ('expression -> expression EQUAL_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',291),
  ('expression -> expression DIFFERENT_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',292),
  ('expression -> expression GREATER_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',293),
  ('expression -> expression GREATER_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',294),
  ('simple_expression -> term expression_action_4','simple_expression',2,'p_simple_expression','eskr_yacc.py',297),
  ('simple_expression -> PLUS term expression_action_4','simple_expression',3,'p_simple_expression','eskr_yacc.py',298),
  ('simple_expression -> MINUS term expression_action_4','simple_expression',3,'p_simple_expression','eskr_yacc.py',299),
  ('simple_expression -> simple_expression OR expression_action_2 term expression_action_4','simple_expression',5,'p_simple_expression','eskr_yacc.py',300),
  ('simple_expression -> simple_expression PLUS expression_action_2 term expression_action_4','simple_expression',5,'p_simple_expression','eskr_yacc.py',301),
  ('simple_expression -> simple_expression MINUS expression_action_2 term expression_action_4','simple_expression',5,'p_simple_expression','eskr_yacc.py',302),
  ('term -> factor','term',1,'p_term','eskr_yacc.py',305),
  ('term -> term TIMES expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',306),
  ('term -> term DIVIDE expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',307),
  ('term -> term MOD expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',308),
  ('term -> term AND expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',309),
  ('factor -> id expression_action_1','factor',2,'p_factor','eskr_yacc.py',314),
  ('factor -> number expression_action_1','factor',2,'p_factor','eskr_yacc.py',315),
  ('factor -> NOT id expression_action_1','factor',3,'p_factor','eskr_yacc.py',316),
  ('factor -> expression_action_6 LPAREN expression RPAREN expression_action_7','factor',5,'p_factor','eskr_yacc.py',317),
  ('number -> real','number',1,'p_number','eskr_yacc.py',325),
  ('number -> integer','number',1,'p_number','eskr_yacc.py',326),
  ('real -> NUMBER DOT NUMBER','real',3,'p_real','eskr_yacc.py',330),
  ('integer -> NUMBER','integer',1,'p_integer','eskr_yacc.py',334),
  ('empty -> <empty>','empty',0,'p_empty','eskr_yacc.py',338),
  ('expression_action_1 -> <empty>','expression_action_1',0,'p_expression_action_1','eskr_yacc.py',347),
  ('expression_action_2 -> <empty>','expression_action_2',0,'p_expression_action_2','eskr_yacc.py',352),
  ('expression_action_3 -> <empty>','expression_action_3',0,'p_expression_action_3','eskr_yacc.py',357),
  ('expression_action_4 -> <empty>','expression_action_4',0,'p_expression_action_4','eskr_yacc.py',362),
  ('expression_action_5 -> <empty>','expression_action_5',0,'p_expression_action_5','eskr_yacc.py',373),
  ('expression_action_6 -> <empty>','expression_action_6',0,'p_expression_action_6','eskr_yacc.py',384),
  ('expression_action_7 -> <empty>','expression_action_7',0,'p_expression_action_7','eskr_yacc.py',389),
  ('expression_action_8 -> <empty>','expression_action_8',0,'p_expression_action_8','eskr_yacc.py',394),
  ('expression_action_9 -> <empty>','expression_action_9',0,'p_expression_action_9','eskr_yacc.py',399),
]
