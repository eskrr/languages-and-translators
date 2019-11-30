
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programAND CIN COMMA COUT DIFFERENT_THAN DIVIDE DO DOT ELSE ENDL EQUAL EQUAL_THAN FLOAT FOR FUNCTION GREATER_OR_EQUAL_THAN GREATER_THAN ID IF INSTREAM INT LBRACE LBRACKET LESS_OR_EQUAL_THAN LESS_THAN LPAREN MAIN MINUS MOD NOT NUMBER OR OUTSTREAM PLUS RBRACE RBRACKET RPAREN SEMICOLON TEXT TIMES WHILEprogram : program_blockprogram_block : declaration SEMICOLON program_block \n                   | assignation SEMICOLON program_block\n                   | normal_function program_block\n                   | main_functionnormal_function : FUNCTION ID start_function_action LPAREN RPAREN function_block end_function_actionmain_function : FUNCTION MAIN start_main_function_action LPAREN RPAREN function_blockstart_function_action : start_main_function_action : end_function_action : function_block : LBRACE instruction RBRACEinstruction : proposition instruction\n                 | emptyproposition : function_call SEMICOLON\n                 | assignation SEMICOLON\n                 | print SEMICOLON\n                 | input SEMICOLON\n                 | unary_operation SEMICOLON\n                 | if_sentence\n                 | while_sentence\n                 | do_while_sentence\n                 | for_sentenceprint : COUT output_expression\n     output_expression : OUTSTREAM expression print_action output_expression\n                       | OUTSTREAM expression print_action\n                       | OUTSTREAM TEXT print_action output_expression\n                       | OUTSTREAM TEXT print_action\n                       | OUTSTREAM ENDL print_action output_expression\n                       | OUTSTREAM ENDL print_action\n  print_action :input : CIN input_expression \n     input_expression : INSTREAM id input_action input_expression\n                      | INSTREAM id input_action  \n  input_action :declaration : type variablestype : INT\n          | FLOATassignation : id assignation_action_1 EQUAL assignation_action_2 expression_1 assignation_action_3assignation_action_1 :assignation_action_2 :assignation_action_3 :unary_operation : ID PLUS PLUS\n                     | ID MINUS MINUS\n                     | PLUS PLUS ID\n                     | MINUS MINUS ID\n  variables   : id COMMA variables\n                 | id\n                 id : ID\n        | ID mark_vector vector\n        | ID mark_vector vector vectormark_vector :vector : LBRACKET integer vector_action RBRACKET\n     vector : LBRACKET ID vector_action RBRACKET\n  vector_action :function_call : ID function_call_action LPAREN RPARENfunction_call_action :if_sentence : IF LPAREN expression_1 RPAREN if_action_1 function_block empty if_action_2\n                 | IF LPAREN expression_1 RPAREN if_action_1 function_block ELSE if_action_2 function_block if_action_3\n  if_action_1 :if_action_2 : if_action_3 :while_sentence : WHILE while_action_1 LPAREN expression_1 RPAREN while_action_2 function_block while_action_3while_action_1 : while_action_2 : while_action_3 : do_while_sentence :  DO do_while_action_1 function_block WHILE LPAREN expression_1 RPAREN do_while_action_2 SEMICOLONdo_while_action_1 : do_while_action_2 : for_sentence : FOR LPAREN for_expression RPAREN function_block for_action_4for_expression : assignation for_action_1 SEMICOLON expression_1 for_action_2 SEMICOLON assignation for_action_3\n                    | assignation for_action_1 SEMICOLON expression_1 for_action_2 SEMICOLON unary_operation for_action_3for_action_1 :for_action_2 :for_action_3 :for_action_4 :expression_1 : expression\n                  | expression AND expression_action_3 expression expression_action_5   expression : simple_expression\n                | expression LESS_THAN expression_action_8 simple_expression expression_action_9   \n                | expression LESS_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9   \n                | expression EQUAL_THAN expression_action_8 simple_expression expression_action_9   \n                | expression DIFFERENT_THAN expression_action_8 simple_expression expression_action_9   \n                | expression GREATER_THAN expression_action_8 simple_expression expression_action_9   \n                | expression GREATER_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9simple_expression : term expression_action_4\n                       | PLUS term expression_action_4\n                       | MINUS term expression_action_4\n                       | simple_expression OR expression_action_2 term expression_action_4\n                       | simple_expression PLUS expression_action_2 term expression_action_4\n                       | simple_expression MINUS expression_action_2 term expression_action_4term : factor\n          | term TIMES expression_action_3 factor expression_action_5\n          | term DIVIDE expression_action_3 factor expression_action_5\n          | term MOD expression_action_3 factor expression_action_5factor : id expression_action_1\n            | number expression_action_1\n            | NOT id expression_action_1\n            | expression_action_6 LPAREN expression RPAREN expression_action_7number : real\n            | integerreal : NUMBER DOT NUMBERinteger : NUMBERempty :expression_action_1 :expression_action_2 :expression_action_3 :expression_action_4 :expression_action_5 :expression_action_6 :expression_action_7 :expression_action_8 :expression_action_9 :'
    
_lr_action_items = {'DO':([78,103,106,107,109,121,140,145,146,147,155,156,201,207,208,210,213,215,218,219,223,226,],[101,-21,101,-20,-22,-19,-14,-16,-17,-18,-15,-11,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'COUT':([78,103,106,107,109,121,140,145,146,147,155,156,201,207,208,210,213,215,218,219,223,226,],[102,-21,102,-20,-22,-19,-14,-16,-17,-18,-15,-11,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'CIN':([78,103,106,107,109,121,140,145,146,147,155,156,201,207,208,210,213,215,218,219,223,226,],[116,-21,116,-20,-22,-19,-14,-16,-17,-18,-15,-11,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'TEXT':([138,],[172,]),'EQUAL':([2,8,13,28,37,81,82,117,221,],[-39,-48,22,-49,-50,-52,-53,-48,-48,]),'LBRACKET':([8,19,28,81,82,117,221,],[-51,27,27,-52,-53,-51,-51,]),'WHILE':([78,103,106,107,109,121,140,145,146,147,155,156,171,201,207,208,210,213,215,218,219,223,226,],[105,-21,105,-20,-22,-19,-14,-16,-17,-18,-15,-11,185,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'DIFFERENT_THAN':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,174,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,74,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,74,-97,-107,-107,-107,-108,-108,-108,-110,74,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,74,]),'LESS_THAN':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,174,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,76,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,76,-97,-107,-107,-107,-108,-108,-108,-110,76,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,76,]),'MINUS':([8,22,28,30,37,38,40,41,42,44,45,46,48,56,60,61,62,67,69,70,71,72,73,74,75,76,77,78,81,82,83,87,88,93,94,95,96,97,98,99,100,103,106,107,108,109,117,121,123,124,125,126,127,128,129,131,132,133,134,135,136,138,140,145,146,147,153,154,155,156,157,158,159,160,161,162,163,175,195,200,201,207,208,210,213,215,216,218,219,221,223,226,],[-48,-40,-49,39,-50,-100,57,-104,-104,-91,-99,-102,-107,-107,-96,-95,-107,-85,39,-106,-111,-111,-111,-111,-111,-111,-104,108,-52,-53,-87,-86,-101,39,39,39,39,39,39,39,-97,-21,108,-20,143,-22,153,-19,-107,-107,-107,-108,-108,-108,-110,57,57,57,57,57,57,39,-14,-16,-17,-18,183,39,-15,-11,-90,-89,-88,-93,-92,-94,-98,39,39,39,-75,-69,-103,-65,-60,-62,108,-57,-66,153,-61,-58,]),'DOT':([46,],[63,]),'RBRACE':([78,103,106,107,109,114,120,121,140,142,145,146,147,155,156,201,207,208,210,213,215,218,219,223,226,],[-103,-21,-103,-20,-22,-13,156,-19,-14,-12,-16,-17,-18,-15,-11,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'RPAREN':([8,28,32,33,37,38,40,41,42,44,45,46,47,48,50,56,60,61,62,64,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,164,165,166,167,168,169,170,176,177,179,181,182,183,184,189,204,220,222,224,225,],[-48,-49,52,53,-50,-100,-78,-104,-104,-91,-99,-102,-41,-107,-76,-107,-96,-95,-107,-38,-85,-104,-52,-53,-87,-86,-101,129,-97,-107,-107,-107,-108,-108,-108,-110,-108,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-77,-81,-84,-80,-82,-83,-79,-45,-44,191,-42,193,-43,194,199,209,-74,-74,-70,-71,]),'SEMICOLON':([7,8,9,14,15,28,31,37,38,40,41,42,44,45,46,47,48,50,56,60,61,62,64,67,77,81,82,83,87,88,100,104,111,112,113,119,123,124,125,126,127,128,129,130,131,132,133,134,135,136,139,150,157,158,159,160,161,162,163,164,165,166,167,168,169,170,172,173,174,176,177,178,180,181,183,186,187,188,190,192,193,196,197,198,202,206,209,211,214,],[18,-48,20,-35,-47,-49,-46,-50,-100,-78,-104,-104,-91,-99,-102,-41,-107,-76,-107,-96,-95,-107,-38,-85,-104,-52,-53,-87,-86,-101,-97,140,145,146,147,155,-107,-107,-107,-108,-108,-108,-110,-108,-112,-112,-112,-112,-112,-112,-23,-31,-90,-89,-88,-93,-92,-94,-98,-77,-81,-84,-80,-82,-83,-79,-30,-30,-30,-45,-44,-72,-34,-42,-43,-27,-29,-25,200,-33,-55,-26,-28,-24,-32,-73,-68,216,219,]),'ENDL':([138,],[173,]),'PLUS':([8,22,28,30,37,38,40,41,42,44,45,46,48,56,60,61,62,67,69,70,71,72,73,74,75,76,77,78,81,82,83,87,88,93,94,95,96,97,98,99,100,103,106,107,109,110,117,121,123,124,125,126,127,128,129,131,132,133,134,135,136,138,140,145,146,147,151,154,155,156,157,158,159,160,161,162,163,175,195,200,201,207,208,210,213,215,216,218,219,221,223,226,],[-48,-40,-49,43,-50,-100,58,-104,-104,-91,-99,-102,-107,-107,-96,-95,-107,-85,43,-106,-111,-111,-111,-111,-111,-111,-104,110,-52,-53,-87,-86,-101,43,43,43,43,43,43,43,-97,-21,110,-20,-22,144,151,-19,-107,-107,-107,-108,-108,-108,-110,58,58,58,58,58,58,43,-14,-16,-17,-18,181,43,-15,-11,-90,-89,-88,-93,-92,-94,-98,43,43,43,-75,-69,-103,-65,-60,-62,110,-57,-66,151,-61,-58,]),'COMMA':([8,15,28,37,81,82,],[-48,23,-49,-50,-52,-53,]),'INSTREAM':([8,28,37,81,82,116,180,192,],[-48,-49,-50,-52,-53,149,-34,149,]),'$end':([1,3,4,21,26,29,79,156,],[-5,0,-1,-4,-2,-3,-7,-11,]),'FUNCTION':([0,11,18,20,80,122,156,],[6,6,6,6,-10,-6,-11,]),'DIVIDE':([8,28,37,38,41,42,44,45,46,48,56,60,61,62,77,81,82,88,100,123,124,125,126,127,128,129,160,161,162,163,],[-48,-49,-50,-100,-104,-104,-91,-99,-102,65,65,-96,-95,65,-104,-52,-53,-101,-97,65,65,65,-108,-108,-108,-110,-93,-92,-94,-98,]),'FOR':([78,103,106,107,109,121,140,145,146,147,155,156,201,207,208,210,213,215,218,219,223,226,],[115,-21,115,-20,-22,-19,-14,-16,-17,-18,-15,-11,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'NUMBER':([22,27,30,39,43,57,58,59,63,65,66,68,69,70,71,72,73,74,75,76,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[-40,34,46,46,46,-105,-105,-105,88,-106,-106,-106,46,-106,-111,-111,-111,-111,-111,-111,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'OUTSTREAM':([8,28,37,38,40,41,42,44,45,46,48,56,60,61,62,67,77,81,82,83,87,88,100,102,123,124,125,126,127,128,129,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,172,173,174,186,187,188,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,-97,138,-107,-107,-107,-108,-108,-108,-110,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,-30,-30,-30,138,138,138,]),'TIMES':([8,28,37,38,41,42,44,45,46,48,56,60,61,62,77,81,82,88,100,123,124,125,126,127,128,129,160,161,162,163,],[-48,-49,-50,-100,-104,-104,-91,-99,-102,66,66,-96,-95,66,-104,-52,-53,-101,-97,66,66,66,-108,-108,-108,-110,-93,-92,-94,-98,]),'LPAREN':([16,17,22,24,25,30,39,43,49,57,58,59,65,66,68,69,70,71,72,73,74,75,76,84,85,86,89,90,91,93,94,95,96,97,98,99,105,115,117,118,138,141,152,154,175,185,195,200,],[-9,-8,-40,32,33,-109,-109,-109,69,-105,-105,-105,-106,-106,-106,-109,-106,-111,-111,-111,-111,-111,-111,-109,-109,-109,-109,-109,-109,-109,-109,-109,-109,-109,-109,-109,-63,148,-56,154,-109,175,182,-109,-109,195,-109,-109,]),'GREATER_THAN':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,174,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,75,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,75,-97,-107,-107,-107,-108,-108,-108,-110,75,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,75,]),'ELSE':([156,208,],[-11,212,]),'ID':([0,5,6,10,11,12,18,20,22,23,27,30,39,43,51,57,58,59,65,66,68,69,70,71,72,73,74,75,76,78,80,84,85,86,89,90,91,93,94,95,96,97,98,99,103,106,107,109,121,122,138,140,143,144,145,146,147,148,149,154,155,156,175,195,200,201,207,208,210,213,215,216,218,219,223,226,],[8,8,17,-36,8,-37,8,8,-40,8,36,8,8,8,8,-105,-105,-105,-106,-106,-106,8,-106,-111,-111,-111,-111,-111,-111,117,-10,8,8,8,8,8,8,8,8,8,8,8,8,8,-21,117,-20,-22,-19,-6,8,-14,176,177,-16,-17,-18,8,8,8,-15,-11,8,8,8,-75,-69,-103,-65,-60,-62,221,-57,-66,-61,-58,]),'IF':([78,103,106,107,109,121,140,145,146,147,155,156,201,207,208,210,213,215,218,219,223,226,],[118,-21,118,-20,-22,-19,-14,-16,-17,-18,-15,-11,-75,-69,-103,-65,-60,-62,-57,-66,-61,-58,]),'AND':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,100,123,124,125,126,127,128,129,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,70,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,-97,-107,-107,-107,-108,-108,-108,-110,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,]),'GREATER_OR_EQUAL_THAN':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,174,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,72,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,72,-97,-107,-107,-107,-108,-108,-108,-110,72,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,72,]),'LBRACE':([52,53,101,137,191,194,199,203,205,212,217,],[78,78,-67,78,78,-59,-64,78,78,-60,78,]),'EQUAL_THAN':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,174,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,71,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,71,-97,-107,-107,-107,-108,-108,-108,-110,71,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,71,]),'INT':([0,11,18,20,80,122,156,],[10,10,10,10,-10,-6,-11,]),'FLOAT':([0,11,18,20,80,122,156,],[12,12,12,12,-10,-6,-11,]),'NOT':([22,30,39,43,57,58,59,65,66,68,69,70,71,72,73,74,75,76,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[-40,51,51,51,-105,-105,-105,-106,-106,-106,51,-106,-111,-111,-111,-111,-111,-111,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'RBRACKET':([34,35,36,54,55,],[-102,-54,-54,81,82,]),'MAIN':([6,],[16,]),'LESS_OR_EQUAL_THAN':([8,28,37,38,40,41,42,44,45,46,48,50,56,60,61,62,67,77,81,82,83,87,88,92,100,123,124,125,126,127,128,129,130,131,132,133,134,135,136,157,158,159,160,161,162,163,165,166,167,168,169,170,174,],[-48,-49,-50,-100,-78,-104,-104,-91,-99,-102,-107,73,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,73,-97,-107,-107,-107,-108,-108,-108,-110,73,-112,-112,-112,-112,-112,-112,-90,-89,-88,-93,-92,-94,-98,-81,-84,-80,-82,-83,-79,73,]),'OR':([8,28,37,38,40,41,42,44,45,46,48,56,60,61,62,67,77,81,82,83,87,88,100,123,124,125,126,127,128,129,131,132,133,134,135,136,157,158,159,160,161,162,163,],[-48,-49,-50,-100,59,-104,-104,-91,-99,-102,-107,-107,-96,-95,-107,-85,-104,-52,-53,-87,-86,-101,-97,-107,-107,-107,-108,-108,-108,-110,59,59,59,59,59,59,-90,-89,-88,-93,-92,-94,-98,]),'MOD':([8,28,37,38,41,42,44,45,46,48,56,60,61,62,77,81,82,88,100,123,124,125,126,127,128,129,160,161,162,163,],[-48,-49,-50,-100,-104,-104,-91,-99,-102,68,68,-96,-95,68,-104,-52,-53,-101,-97,68,68,68,-108,-108,-108,-110,-93,-92,-94,-98,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'main_function':([0,11,18,20,],[1,1,1,1,]),'do_while_sentence':([78,106,],[103,103,]),'assignation_action_2':([22,],[30,]),'assignation_action_3':([47,],[64,]),'variables':([5,23,],[14,31,]),'assignation_action_1':([2,],[13,]),'do_while_action_1':([101,],[137,]),'number':([30,39,43,69,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'function_call':([78,106,],[104,104,]),'proposition':([78,106,],[106,106,]),'do_while_action_2':([209,],[214,]),'if_action_2':([212,213,],[217,218,]),'while_sentence':([78,106,],[107,107,]),'simple_expression':([30,69,93,94,95,96,97,98,99,138,154,175,195,200,],[40,40,40,131,132,133,134,135,136,40,40,40,40,40,]),'id':([0,5,11,18,20,23,30,39,43,51,69,78,84,85,86,89,90,91,93,94,95,96,97,98,99,106,138,148,149,154,175,195,200,216,],[2,15,2,2,2,15,42,42,42,77,42,2,42,42,42,42,42,42,42,42,42,42,42,42,42,2,42,2,180,42,42,42,42,2,]),'expression_action_2':([57,58,59,],[84,85,86,]),'end_function_action':([80,],[122,]),'mark_vector':([8,117,221,],[19,19,19,]),'instruction':([78,106,],[120,142,]),'if_action_1':([194,],[203,]),'start_main_function_action':([16,],[24,]),'if_action_3':([223,],[226,]),'vector_action':([35,36,],[54,55,]),'program':([0,],[3,]),'factor':([30,39,43,69,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[44,44,44,44,44,44,44,126,127,128,44,44,44,44,44,44,44,44,44,44,44,44,]),'print':([78,106,],[111,111,]),'input':([78,106,],[112,112,]),'type':([0,11,18,20,],[5,5,5,5,]),'empty':([78,106,208,],[114,114,213,]),'real':([30,39,43,69,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'unary_operation':([78,106,216,],[113,113,222,]),'function_call_action':([117,],[152,]),'input_action':([180,],[192,]),'for_expression':([148,],[179,]),'while_action_3':([210,],[215,]),'expression_1':([30,154,175,195,200,],[47,184,189,204,206,]),'program_block':([0,11,18,20,],[4,21,26,29,]),'for_action_1':([178,],[190,]),'while_action_2':([199,],[205,]),'expression_action_5':([126,127,128,130,],[160,161,162,164,]),'start_function_action':([17,],[25,]),'expression_action_7':([129,],[163,]),'expression_action_6':([30,39,43,69,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'expression_action_1':([41,42,77,],[60,61,100,]),'while_action_1':([105,],[141,]),'expression_action_3':([65,66,68,70,],[89,90,91,93,]),'declaration':([0,11,18,20,],[7,7,7,7,]),'function_block':([52,53,137,191,203,205,217,],[79,80,171,201,208,210,223,]),'integer':([27,30,39,43,69,84,85,86,89,90,91,93,94,95,96,97,98,99,138,154,175,195,200,],[35,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'expression_action_9':([131,132,133,134,135,136,],[165,166,167,168,169,170,]),'expression_action_8':([71,72,73,74,75,76,],[94,95,96,97,98,99,]),'for_action_3':([220,222,],[224,225,]),'for_action_2':([206,],[211,]),'term':([30,39,43,69,84,85,86,93,94,95,96,97,98,99,138,154,175,195,200,],[48,56,62,48,123,124,125,48,48,48,48,48,48,48,48,48,48,48,48,]),'assignation':([0,11,18,20,78,106,148,216,],[9,9,9,9,119,119,178,220,]),'expression_action_4':([48,56,62,123,124,125,],[67,83,87,157,158,159,]),'if_sentence':([78,106,],[121,121,]),'normal_function':([0,11,18,20,],[11,11,11,11,]),'input_expression':([116,192,],[150,202,]),'output_expression':([102,186,187,188,],[139,196,197,198,]),'vector':([19,28,],[28,37,]),'print_action':([172,173,174,],[186,187,188,]),'expression':([30,69,93,138,154,175,195,200,],[50,92,130,174,50,50,50,50,]),'for_sentence':([78,106,],[109,109,]),'for_action_4':([201,],[207,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program_block','program',1,'p_program','eskr_yacc.py',37),
  ('program_block -> declaration SEMICOLON program_block','program_block',3,'p_program_block','eskr_yacc.py',40),
  ('program_block -> assignation SEMICOLON program_block','program_block',3,'p_program_block','eskr_yacc.py',41),
  ('program_block -> normal_function program_block','program_block',2,'p_program_block','eskr_yacc.py',42),
  ('program_block -> main_function','program_block',1,'p_program_block','eskr_yacc.py',43),
  ('normal_function -> FUNCTION ID start_function_action LPAREN RPAREN function_block end_function_action','normal_function',7,'p_normal_function','eskr_yacc.py',46),
  ('main_function -> FUNCTION MAIN start_main_function_action LPAREN RPAREN function_block','main_function',6,'p_main_function','eskr_yacc.py',49),
  ('start_function_action -> <empty>','start_function_action',0,'p_start_function_action','eskr_yacc.py',52),
  ('start_main_function_action -> <empty>','start_main_function_action',0,'p_start_main_function_action','eskr_yacc.py',57),
  ('end_function_action -> <empty>','end_function_action',0,'p_end_function_action','eskr_yacc.py',62),
  ('function_block -> LBRACE instruction RBRACE','function_block',3,'p_function_block','eskr_yacc.py',67),
  ('instruction -> proposition instruction','instruction',2,'p_instruction','eskr_yacc.py',70),
  ('instruction -> empty','instruction',1,'p_instruction','eskr_yacc.py',71),
  ('proposition -> function_call SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',74),
  ('proposition -> assignation SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',75),
  ('proposition -> print SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',76),
  ('proposition -> input SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',77),
  ('proposition -> unary_operation SEMICOLON','proposition',2,'p_proposition','eskr_yacc.py',78),
  ('proposition -> if_sentence','proposition',1,'p_proposition','eskr_yacc.py',79),
  ('proposition -> while_sentence','proposition',1,'p_proposition','eskr_yacc.py',80),
  ('proposition -> do_while_sentence','proposition',1,'p_proposition','eskr_yacc.py',81),
  ('proposition -> for_sentence','proposition',1,'p_proposition','eskr_yacc.py',82),
  ('print -> COUT output_expression','print',2,'p_print','eskr_yacc.py',85),
  ('output_expression -> OUTSTREAM expression print_action output_expression','output_expression',4,'p_print','eskr_yacc.py',86),
  ('output_expression -> OUTSTREAM expression print_action','output_expression',3,'p_print','eskr_yacc.py',87),
  ('output_expression -> OUTSTREAM TEXT print_action output_expression','output_expression',4,'p_print','eskr_yacc.py',88),
  ('output_expression -> OUTSTREAM TEXT print_action','output_expression',3,'p_print','eskr_yacc.py',89),
  ('output_expression -> OUTSTREAM ENDL print_action output_expression','output_expression',4,'p_print','eskr_yacc.py',90),
  ('output_expression -> OUTSTREAM ENDL print_action','output_expression',3,'p_print','eskr_yacc.py',91),
  ('print_action -> <empty>','print_action',0,'p_print_action','eskr_yacc.py',95),
  ('input -> CIN input_expression','input',2,'p_input','eskr_yacc.py',107),
  ('input_expression -> INSTREAM id input_action input_expression','input_expression',4,'p_input','eskr_yacc.py',108),
  ('input_expression -> INSTREAM id input_action','input_expression',3,'p_input','eskr_yacc.py',109),
  ('input_action -> <empty>','input_action',0,'p_input_action','eskr_yacc.py',113),
  ('declaration -> type variables','declaration',2,'p_declaration','eskr_yacc.py',120),
  ('type -> INT','type',1,'p_type','eskr_yacc.py',139),
  ('type -> FLOAT','type',1,'p_type','eskr_yacc.py',140),
  ('assignation -> id assignation_action_1 EQUAL assignation_action_2 expression_1 assignation_action_3','assignation',6,'p_assignation','eskr_yacc.py',144),
  ('assignation_action_1 -> <empty>','assignation_action_1',0,'p_assignation_action_1','eskr_yacc.py',147),
  ('assignation_action_2 -> <empty>','assignation_action_2',0,'p_assignation_action_2','eskr_yacc.py',165),
  ('assignation_action_3 -> <empty>','assignation_action_3',0,'p_assignation_action_3','eskr_yacc.py',170),
  ('unary_operation -> ID PLUS PLUS','unary_operation',3,'p_unary_operation','eskr_yacc.py',177),
  ('unary_operation -> ID MINUS MINUS','unary_operation',3,'p_unary_operation','eskr_yacc.py',178),
  ('unary_operation -> PLUS PLUS ID','unary_operation',3,'p_unary_operation','eskr_yacc.py',179),
  ('unary_operation -> MINUS MINUS ID','unary_operation',3,'p_unary_operation','eskr_yacc.py',180),
  ('variables -> id COMMA variables','variables',3,'p_variables','eskr_yacc.py',186),
  ('variables -> id','variables',1,'p_variables','eskr_yacc.py',187),
  ('id -> ID','id',1,'p_id','eskr_yacc.py',195),
  ('id -> ID mark_vector vector','id',3,'p_id','eskr_yacc.py',196),
  ('id -> ID mark_vector vector vector','id',4,'p_id','eskr_yacc.py',197),
  ('mark_vector -> <empty>','mark_vector',0,'p_mark_vector','eskr_yacc.py',201),
  ('vector -> LBRACKET integer vector_action RBRACKET','vector',4,'p_vector','eskr_yacc.py',206),
  ('vector -> LBRACKET ID vector_action RBRACKET','vector',4,'p_vector','eskr_yacc.py',207),
  ('vector_action -> <empty>','vector_action',0,'p_vector_action','eskr_yacc.py',211),
  ('function_call -> ID function_call_action LPAREN RPAREN','function_call',4,'p_function_call','eskr_yacc.py',216),
  ('function_call_action -> <empty>','function_call_action',0,'p_function_call_action','eskr_yacc.py',219),
  ('if_sentence -> IF LPAREN expression_1 RPAREN if_action_1 function_block empty if_action_2','if_sentence',8,'p_if_sentence','eskr_yacc.py',225),
  ('if_sentence -> IF LPAREN expression_1 RPAREN if_action_1 function_block ELSE if_action_2 function_block if_action_3','if_sentence',10,'p_if_sentence','eskr_yacc.py',226),
  ('if_action_1 -> <empty>','if_action_1',0,'p_if_action_1','eskr_yacc.py',230),
  ('if_action_2 -> <empty>','if_action_2',0,'p_if_action_2','eskr_yacc.py',236),
  ('if_action_3 -> <empty>','if_action_3',0,'p_if_action_3','eskr_yacc.py',246),
  ('while_sentence -> WHILE while_action_1 LPAREN expression_1 RPAREN while_action_2 function_block while_action_3','while_sentence',8,'p_while_sentence','eskr_yacc.py',252),
  ('while_action_1 -> <empty>','while_action_1',0,'p_while_action_1','eskr_yacc.py',255),
  ('while_action_2 -> <empty>','while_action_2',0,'p_while_action_2','eskr_yacc.py',260),
  ('while_action_3 -> <empty>','while_action_3',0,'p_while_action_3','eskr_yacc.py',266),
  ('do_while_sentence -> DO do_while_action_1 function_block WHILE LPAREN expression_1 RPAREN do_while_action_2 SEMICOLON','do_while_sentence',9,'p_do_while_sentence','eskr_yacc.py',273),
  ('do_while_action_1 -> <empty>','do_while_action_1',0,'p_do_while_action_1','eskr_yacc.py',276),
  ('do_while_action_2 -> <empty>','do_while_action_2',0,'p_do_while_action_2','eskr_yacc.py',281),
  ('for_sentence -> FOR LPAREN for_expression RPAREN function_block for_action_4','for_sentence',6,'p_for_sentence','eskr_yacc.py',286),
  ('for_expression -> assignation for_action_1 SEMICOLON expression_1 for_action_2 SEMICOLON assignation for_action_3','for_expression',8,'p_for_expression','eskr_yacc.py',289),
  ('for_expression -> assignation for_action_1 SEMICOLON expression_1 for_action_2 SEMICOLON unary_operation for_action_3','for_expression',8,'p_for_expression','eskr_yacc.py',290),
  ('for_action_1 -> <empty>','for_action_1',0,'p_for_action_1','eskr_yacc.py',293),
  ('for_action_2 -> <empty>','for_action_2',0,'p_for_action_2','eskr_yacc.py',298),
  ('for_action_3 -> <empty>','for_action_3',0,'p_for_action_3','eskr_yacc.py',310),
  ('for_action_4 -> <empty>','for_action_4',0,'p_for_action_4','eskr_yacc.py',316),
  ('expression_1 -> expression','expression_1',1,'p_expression_1','eskr_yacc.py',322),
  ('expression_1 -> expression AND expression_action_3 expression expression_action_5','expression_1',5,'p_expression_1','eskr_yacc.py',323),
  ('expression -> simple_expression','expression',1,'p_expression','eskr_yacc.py',326),
  ('expression -> expression LESS_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',327),
  ('expression -> expression LESS_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',328),
  ('expression -> expression EQUAL_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',329),
  ('expression -> expression DIFFERENT_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',330),
  ('expression -> expression GREATER_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',331),
  ('expression -> expression GREATER_OR_EQUAL_THAN expression_action_8 simple_expression expression_action_9','expression',5,'p_expression','eskr_yacc.py',332),
  ('simple_expression -> term expression_action_4','simple_expression',2,'p_simple_expression','eskr_yacc.py',335),
  ('simple_expression -> PLUS term expression_action_4','simple_expression',3,'p_simple_expression','eskr_yacc.py',336),
  ('simple_expression -> MINUS term expression_action_4','simple_expression',3,'p_simple_expression','eskr_yacc.py',337),
  ('simple_expression -> simple_expression OR expression_action_2 term expression_action_4','simple_expression',5,'p_simple_expression','eskr_yacc.py',338),
  ('simple_expression -> simple_expression PLUS expression_action_2 term expression_action_4','simple_expression',5,'p_simple_expression','eskr_yacc.py',339),
  ('simple_expression -> simple_expression MINUS expression_action_2 term expression_action_4','simple_expression',5,'p_simple_expression','eskr_yacc.py',340),
  ('term -> factor','term',1,'p_term','eskr_yacc.py',343),
  ('term -> term TIMES expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',344),
  ('term -> term DIVIDE expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',345),
  ('term -> term MOD expression_action_3 factor expression_action_5','term',5,'p_term','eskr_yacc.py',346),
  ('factor -> id expression_action_1','factor',2,'p_factor','eskr_yacc.py',351),
  ('factor -> number expression_action_1','factor',2,'p_factor','eskr_yacc.py',352),
  ('factor -> NOT id expression_action_1','factor',3,'p_factor','eskr_yacc.py',353),
  ('factor -> expression_action_6 LPAREN expression RPAREN expression_action_7','factor',5,'p_factor','eskr_yacc.py',354),
  ('number -> real','number',1,'p_number','eskr_yacc.py',362),
  ('number -> integer','number',1,'p_number','eskr_yacc.py',363),
  ('real -> NUMBER DOT NUMBER','real',3,'p_real','eskr_yacc.py',367),
  ('integer -> NUMBER','integer',1,'p_integer','eskr_yacc.py',371),
  ('empty -> <empty>','empty',0,'p_empty','eskr_yacc.py',375),
  ('expression_action_1 -> <empty>','expression_action_1',0,'p_expression_action_1','eskr_yacc.py',384),
  ('expression_action_2 -> <empty>','expression_action_2',0,'p_expression_action_2','eskr_yacc.py',398),
  ('expression_action_3 -> <empty>','expression_action_3',0,'p_expression_action_3','eskr_yacc.py',403),
  ('expression_action_4 -> <empty>','expression_action_4',0,'p_expression_action_4','eskr_yacc.py',408),
  ('expression_action_5 -> <empty>','expression_action_5',0,'p_expression_action_5','eskr_yacc.py',419),
  ('expression_action_6 -> <empty>','expression_action_6',0,'p_expression_action_6','eskr_yacc.py',430),
  ('expression_action_7 -> <empty>','expression_action_7',0,'p_expression_action_7','eskr_yacc.py',435),
  ('expression_action_8 -> <empty>','expression_action_8',0,'p_expression_action_8','eskr_yacc.py',440),
  ('expression_action_9 -> <empty>','expression_action_9',0,'p_expression_action_9','eskr_yacc.py',445),
]
