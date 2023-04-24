
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLOGICAL_ORleftLOGICAL_ANDleftEQUALSNOT_EQUALSleftLESS_THANLESS_THAN_OR_EQUALGREATER_THANGREATER_THAN_OR_EQUALleftPLUSMINUSleftMULTIPLYDIVIDEMODULUSrightLOGICAL_NOTnonassocEQUALSASSIGN COMMA DIVIDE DO ELIF ELSE EQUALS FALSE FLOAT GREATER_THAN GREATER_THAN_OR_EQUAL IDENTIFIER IF INTEGER LBRACE LESS_THAN LESS_THAN_OR_EQUAL LOGICAL_AND LOGICAL_NOT LOGICAL_OR LPAREN MAIN MINUS MODULUS MULTIPLY NOT_EQUALS PLUS PRINT RBRACE RETURN RPAREN SEMICOLON STRING TRUE TYPE_BOOL TYPE_FLOAT TYPE_INT VOID WHILE\n    program : function main_function\n            | main_function\n    \n    main_function : TYPE_INT MAIN LPAREN RPAREN LBRACE statement_list RBRACE\n    \n    statement_list : statement\n                   | statement statement_list\n    \n    statement : expression_statement\n              | control_statement\n              | return_statement\n              | print_statement\n    \n    expression_statement : expression SEMICOLON\n    \n    control_statement : if_statement\n                      | while_statement\n                      | do_while_statement\n    \n    type_keyword : TYPE_INT\n                 | TYPE_BOOL\n                 | TYPE_FLOAT\n    \n    if_statement : IF LPAREN expression RPAREN LBRACE statement RBRACE\n                 | IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE\n                 | IF LPAREN expression RPAREN LBRACE statement RBRACE ELIF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE\n    \n    while_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE\n    do_while_statement : DO LBRACE statement RBRACE WHILE LPAREN expression RPARENreturn_statement : RETURN LPAREN INTEGER RPAREN SEMICOLON\n                        | RETURN LPAREN FLOAT RPAREN SEMICOLON\n                        | RETURN LPAREN TRUE RPAREN SEMICOLON\n                        | RETURN LPAREN FALSE RPAREN SEMICOLON\n    \n    print_statement : PRINT LPAREN STRING RPAREN SEMICOLON\n    \n    expression  : assignment_expression\n                | logical_expression\n                | unary_expression\n                | arithmetic_expression\n                | relational_expression\n                | equality_expression\n    \n    arithmetic_expression   : IDENTIFIER PLUS IDENTIFIER\n                            | IDENTIFIER PLUS INTEGER\n                            | IDENTIFIER MODULUS IDENTIFIER\n                            | IDENTIFIER MINUS IDENTIFIER\n                            | IDENTIFIER MINUS INTEGER\n                            | IDENTIFIER MINUS FLOAT\n                            | IDENTIFIER MODULUS INTEGER\n                            | IDENTIFIER MULTIPLY IDENTIFIER\n                            | IDENTIFIER MULTIPLY INTEGER\n                            | IDENTIFIER MULTIPLY FLOAT\n                            | IDENTIFIER DIVIDE IDENTIFIER\n                            | IDENTIFIER DIVIDE INTEGER\n                            | IDENTIFIER DIVIDE FLOAT\n                            | INTEGER PLUS INTEGER\n                            | INTEGER PLUS IDENTIFIER\n                            | INTEGER MODULUS IDENTIFIER\n                            | INTEGER MODULUS INTEGER\n\n    \n    assignment_expression : type_keyword IDENTIFIER ASSIGN INTEGER\n                          | type_keyword IDENTIFIER ASSIGN FLOAT\n                          | type_keyword IDENTIFIER ASSIGN TRUE\n                          | type_keyword IDENTIFIER ASSIGN FALSE\n                          | type_keyword IDENTIFIER ASSIGN arithmetic_expression\n                          | type_keyword IDENTIFIER ASSIGN function_call\n                          | IDENTIFIER ASSIGN INTEGER\n                          | IDENTIFIER ASSIGN FLOAT\n                          | IDENTIFIER ASSIGN TRUE\n                          | IDENTIFIER ASSIGN FALSE\n                          | IDENTIFIER ASSIGN arithmetic_expression\n                          | IDENTIFIER ASSIGN function_call\n\n    \n    logical_expression : logical_or_expression\n                       | logical_and_expression\n                       | logical_not_expression\n    \n    logical_or_expression   : IDENTIFIER LOGICAL_OR IDENTIFIER\n                            | IDENTIFIER LOGICAL_OR relational_expression\n                            | IDENTIFIER LOGICAL_OR equality_expression\n                            | relational_expression LOGICAL_OR IDENTIFIER\n                            | relational_expression LOGICAL_OR relational_expression\n                            | relational_expression LOGICAL_OR equality_expression\n                            | equality_expression LOGICAL_OR IDENTIFIER\n                            | equality_expression LOGICAL_OR relational_expression\n                            | equality_expression LOGICAL_OR equality_expression\n    \n    logical_and_expression : IDENTIFIER LOGICAL_AND IDENTIFIER\n                           | IDENTIFIER LOGICAL_AND relational_expression\n                           | IDENTIFIER LOGICAL_AND equality_expression\n                           | relational_expression LOGICAL_AND IDENTIFIER\n                           | relational_expression LOGICAL_AND relational_expression\n                           | relational_expression LOGICAL_AND equality_expression\n                           | equality_expression LOGICAL_AND IDENTIFIER\n                           | equality_expression LOGICAL_AND relational_expression\n                           | equality_expression LOGICAL_AND equality_expression\n\n    logical_not_expression   : LOGICAL_NOT logical_and_expression\n                                | LOGICAL_NOT logical_or_expression\n                                | LOGICAL_NOT IDENTIFIER\n                                | LOGICAL_NOT equality_expression\n                                | LOGICAL_NOT relational_expression\n    equality_expression : IDENTIFIER EQUALS IDENTIFIER\n                           | IDENTIFIER EQUALS INTEGER\n                           | IDENTIFIER EQUALS FLOAT\n                           | IDENTIFIER EQUALS TRUE\n                           | IDENTIFIER EQUALS FALSE\n                           | IDENTIFIER NOT_EQUALS IDENTIFIER\n                           | IDENTIFIER NOT_EQUALS INTEGER\n                           | IDENTIFIER NOT_EQUALS FLOAT\n                           | IDENTIFIER NOT_EQUALS TRUE\n                           | IDENTIFIER NOT_EQUALS FALSE\n     relational_expression   : IDENTIFIER GREATER_THAN IDENTIFIER\n                                | IDENTIFIER GREATER_THAN INTEGER\n                                | IDENTIFIER GREATER_THAN FLOAT\n                                | IDENTIFIER LESS_THAN IDENTIFIER\n                                | IDENTIFIER LESS_THAN INTEGER\n                                | IDENTIFIER LESS_THAN FLOAT\n                                | IDENTIFIER LESS_THAN_OR_EQUAL IDENTIFIER\n                                | IDENTIFIER LESS_THAN_OR_EQUAL INTEGER\n                                | IDENTIFIER LESS_THAN_OR_EQUAL FLOAT\n                                | IDENTIFIER GREATER_THAN_OR_EQUAL IDENTIFIER\n                                | IDENTIFIER GREATER_THAN_OR_EQUAL INTEGER\n                                | IDENTIFIER GREATER_THAN_OR_EQUAL FLOAT\n                                | INTEGER GREATER_THAN IDENTIFIER\n                                | INTEGER GREATER_THAN INTEGER\n                                | INTEGER GREATER_THAN FLOAT\n                                | INTEGER LESS_THAN IDENTIFIER\n                                | INTEGER LESS_THAN INTEGER\n                                | INTEGER LESS_THAN FLOAT\n                                | INTEGER LESS_THAN_OR_EQUAL IDENTIFIER\n                                | INTEGER LESS_THAN_OR_EQUAL INTEGER\n                                | INTEGER LESS_THAN_OR_EQUAL FLOAT\n                                | INTEGER GREATER_THAN_OR_EQUAL IDENTIFIER\n                                | INTEGER GREATER_THAN_OR_EQUAL INTEGER\n                                | INTEGER GREATER_THAN_OR_EQUAL FLOAT\n                                | FLOAT GREATER_THAN IDENTIFIER\n                                | FLOAT GREATER_THAN INTEGER\n                                | FLOAT GREATER_THAN FLOAT\n                                | FLOAT LESS_THAN IDENTIFIER\n                                | FLOAT LESS_THAN INTEGER\n                                | FLOAT LESS_THAN FLOAT\n                                | FLOAT LESS_THAN_OR_EQUAL IDENTIFIER\n                                | FLOAT LESS_THAN_OR_EQUAL INTEGER\n                                | FLOAT LESS_THAN_OR_EQUAL FLOAT\n                                | FLOAT GREATER_THAN_OR_EQUAL IDENTIFIER\n                                | FLOAT GREATER_THAN_OR_EQUAL INTEGER\n                                | FLOAT GREATER_THAN_OR_EQUAL FLOAT\n    unary_expression   : MINUS number\n                          | PLUS number\n                          | function_call\n                          | IDENTIFIER\n                          | LPAREN expression RPAREN\n    \n    function : type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE\n    function : VOID IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE\n    function_call : IDENTIFIER LPAREN argument_list RPAREN \n    argument_list : argument\n                  | argument COMMA argument_list\n    \n    argument : type_keyword IDENTIFIER\n    number   : INTEGER\n                | FLOAT'
    
_lr_action_items = {'VOID':([0,],[5,]),'TYPE_INT':([0,2,14,15,25,27,28,30,31,33,34,35,36,37,39,40,41,69,86,87,88,104,115,116,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[6,10,20,20,20,20,20,20,20,20,-6,-7,-8,-9,-11,-12,-13,-10,20,20,20,20,-139,-140,-22,-23,-24,-25,-26,20,20,20,-17,-20,-21,20,20,-18,20,20,-19,]),'TYPE_BOOL':([0,14,15,25,27,28,30,31,33,34,35,36,37,39,40,41,69,86,87,88,104,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[7,7,7,7,7,7,7,7,7,-6,-7,-8,-9,-11,-12,-13,-10,7,7,7,7,-22,-23,-24,-25,-26,7,7,7,-17,-20,-21,7,7,-18,7,7,-19,]),'TYPE_FLOAT':([0,14,15,25,27,28,30,31,33,34,35,36,37,39,40,41,69,86,87,88,104,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[8,8,8,8,8,8,8,8,8,-6,-7,-8,-9,-11,-12,-13,-10,8,8,8,8,-22,-23,-24,-25,-26,8,8,8,-17,-20,-21,8,8,-18,8,8,-19,]),'$end':([1,3,9,67,],[0,-2,-1,-3,]),'IDENTIFIER':([4,5,6,7,8,17,20,27,28,30,31,33,34,35,36,37,39,40,41,55,63,69,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,166,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[11,12,-14,-15,-16,23,-14,56,56,56,56,56,-6,-7,-8,-9,-11,-12,-13,89,111,-10,123,125,127,130,133,136,139,142,145,148,152,155,158,161,56,56,56,167,174,176,178,181,184,187,190,193,196,199,204,209,212,167,-22,-23,-24,-25,-26,56,56,56,-17,-20,-21,56,56,-18,56,56,-19,]),'MAIN':([6,10,],[13,13,]),'LPAREN':([11,12,13,27,28,30,31,33,34,35,36,37,39,40,41,42,45,52,53,56,69,86,87,88,167,231,232,233,234,235,236,237,238,241,242,243,246,247,248,249,252,254,258,260,],[14,15,16,31,31,31,31,31,-6,-7,-8,-9,-11,-12,-13,70,81,86,87,104,-10,31,31,31,104,-22,-23,-24,-25,-26,31,31,241,31,-17,-20,249,-21,31,31,-18,31,31,-19,]),'RPAREN':([16,18,19,21,23,29,46,47,48,49,50,51,56,57,58,59,60,66,105,106,107,108,109,110,111,112,113,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,224,225,226,227,228,229,230,244,251,],[22,24,-142,26,-144,-143,-27,-28,-29,-30,-31,-32,-137,-136,-62,-63,-64,117,-134,-145,-146,-135,-83,-84,-85,-86,-87,-138,216,217,218,219,-46,-47,-49,-48,-111,-110,-112,-114,-113,-115,-117,-116,-118,-120,-119,-121,-124,-122,-123,-127,-125,-126,-130,-128,-129,-133,-131,-132,220,-69,-68,-70,-78,-77,-79,-73,-71,-72,-82,-80,-81,221,222,-56,-57,-58,-59,-60,-61,-33,-34,-35,-39,-36,-37,-38,-40,-41,-42,-43,-44,-45,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-65,-66,-67,-74,-75,-76,230,-50,-51,-52,-53,-54,-55,-141,247,253,]),'COMMA':([19,23,],[25,-144,]),'LBRACE':([22,24,26,54,221,222,245,253,257,],[27,28,30,88,236,237,248,254,258,]),'RETURN':([27,28,30,33,34,35,36,37,39,40,41,69,88,231,232,233,234,235,236,237,242,243,247,248,252,254,258,260,],[42,42,42,42,-6,-7,-8,-9,-11,-12,-13,-10,42,-22,-23,-24,-25,-26,42,42,-17,-20,-21,42,-18,42,42,-19,]),'PRINT':([27,28,30,33,34,35,36,37,39,40,41,69,88,231,232,233,234,235,236,237,242,243,247,248,252,254,258,260,],[45,45,45,45,-6,-7,-8,-9,-11,-12,-13,-10,45,-22,-23,-24,-25,-26,45,45,-17,-20,-21,45,-18,45,45,-19,]),'IF':([27,28,30,33,34,35,36,37,39,40,41,69,88,231,232,233,234,235,236,237,242,243,247,248,252,254,258,260,],[52,52,52,52,-6,-7,-8,-9,-11,-12,-13,-10,52,-22,-23,-24,-25,-26,52,52,-17,-20,-21,52,-18,52,52,-19,]),'WHILE':([27,28,30,33,34,35,36,37,39,40,41,69,88,223,231,232,233,234,235,236,237,242,243,247,248,252,254,258,260,],[53,53,53,53,-6,-7,-8,-9,-11,-12,-13,-10,53,238,-22,-23,-24,-25,-26,53,53,-17,-20,-21,53,-18,53,53,-19,]),'DO':([27,28,30,33,34,35,36,37,39,40,41,69,88,231,232,233,234,235,236,237,242,243,247,248,252,254,258,260,],[54,54,54,54,-6,-7,-8,-9,-11,-12,-13,-10,54,-22,-23,-24,-25,-26,54,54,-17,-20,-21,54,-18,54,54,-19,]),'MINUS':([27,28,30,31,33,34,35,36,37,39,40,41,56,69,86,87,88,167,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[61,61,61,61,61,-6,-7,-8,-9,-11,-12,-13,93,-10,61,61,61,93,-22,-23,-24,-25,-26,61,61,61,-17,-20,-21,61,61,-18,61,61,-19,]),'PLUS':([27,28,30,31,33,34,35,36,37,39,40,41,43,56,69,86,87,88,167,168,224,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[62,62,62,62,62,-6,-7,-8,-9,-11,-12,-13,71,91,-10,62,62,62,91,71,71,-22,-23,-24,-25,-26,62,62,62,-17,-20,-21,62,62,-18,62,62,-19,]),'INTEGER':([27,28,30,31,33,34,35,36,37,39,40,41,61,62,63,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,100,101,102,103,166,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[43,43,43,43,43,-6,-7,-8,-9,-11,-12,-13,106,106,114,-10,118,122,124,126,129,132,135,140,143,146,149,114,114,114,114,43,43,43,168,175,177,179,182,185,188,191,194,197,200,205,114,114,224,-22,-23,-24,-25,-26,43,43,43,-17,-20,-21,43,43,-18,43,43,-19,]),'FLOAT':([27,28,30,31,33,34,35,36,37,39,40,41,61,62,63,69,70,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,90,93,94,95,96,97,98,99,100,101,102,103,166,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[44,44,44,44,44,-6,-7,-8,-9,-11,-12,-13,107,107,44,-10,119,128,131,134,137,138,141,144,147,44,44,44,44,44,44,44,169,180,183,186,189,192,195,198,201,206,44,44,225,-22,-23,-24,-25,-26,44,44,44,-17,-20,-21,44,44,-18,44,44,-19,]),'LOGICAL_NOT':([27,28,30,31,33,34,35,36,37,39,40,41,69,86,87,88,231,232,233,234,235,236,237,241,242,243,247,248,249,252,254,258,260,],[63,63,63,63,63,-6,-7,-8,-9,-11,-12,-13,-10,63,63,63,-22,-23,-24,-25,-26,63,63,63,-17,-20,-21,63,63,-18,63,63,-19,]),'RBRACE':([32,33,34,35,36,37,39,40,41,64,65,68,69,165,231,232,233,234,235,239,240,242,243,247,250,252,255,259,260,],[67,-4,-6,-7,-8,-9,-11,-12,-13,115,116,-5,-10,223,-22,-23,-24,-25,-26,242,243,-17,-20,-21,252,-18,256,260,-19,]),'SEMICOLON':([38,46,47,48,49,50,51,56,57,58,59,60,105,106,107,108,109,110,111,112,113,117,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,151,152,153,154,155,156,157,158,159,160,161,162,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,216,217,218,219,220,224,225,226,227,228,229,230,],[69,-27,-28,-29,-30,-31,-32,-137,-136,-62,-63,-64,-134,-145,-146,-135,-83,-84,-85,-86,-87,-138,-46,-47,-49,-48,-111,-110,-112,-114,-113,-115,-117,-116,-118,-120,-119,-121,-124,-122,-123,-127,-125,-126,-130,-128,-129,-133,-131,-132,-69,-68,-70,-78,-77,-79,-73,-71,-72,-82,-80,-81,-56,-57,-58,-59,-60,-61,-33,-34,-35,-39,-36,-37,-38,-40,-41,-42,-43,-44,-45,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,-65,-66,-67,-74,-75,-76,231,232,233,234,235,-50,-51,-52,-53,-54,-55,-141,]),'MODULUS':([43,56,167,168,224,],[72,92,92,72,72,]),'GREATER_THAN':([43,44,56,111,114,152,155,158,161,209,212,],[73,77,96,96,73,96,96,96,96,96,96,]),'LESS_THAN':([43,44,56,111,114,152,155,158,161,209,212,],[74,78,97,97,74,97,97,97,97,97,97,]),'LESS_THAN_OR_EQUAL':([43,44,56,111,114,152,155,158,161,209,212,],[75,79,98,98,75,98,98,98,98,98,98,]),'GREATER_THAN_OR_EQUAL':([43,44,56,111,114,152,155,158,161,209,212,],[76,80,99,99,76,99,99,99,99,99,99,]),'LOGICAL_OR':([50,51,56,111,112,113,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,],[82,84,102,102,84,82,-111,-110,-112,-114,-113,-115,-117,-116,-118,-120,-119,-121,-124,-122,-123,-127,-125,-126,-130,-128,-129,-133,-131,-132,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,]),'LOGICAL_AND':([50,51,56,111,112,113,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,],[83,85,103,103,85,83,-111,-110,-112,-114,-113,-115,-117,-116,-118,-120,-119,-121,-124,-122,-123,-127,-125,-126,-130,-128,-129,-133,-131,-132,-98,-99,-100,-101,-102,-103,-104,-105,-106,-107,-108,-109,-88,-89,-90,-91,-92,-93,-94,-95,-96,-97,]),'ASSIGN':([56,89,],[90,166,]),'MULTIPLY':([56,167,],[94,94,]),'DIVIDE':([56,167,],[95,95,]),'EQUALS':([56,111,152,155,158,161,209,212,],[100,100,100,100,100,100,100,100,]),'NOT_EQUALS':([56,111,152,155,158,161,209,212,],[101,101,101,101,101,101,101,101,]),'TRUE':([70,90,100,101,166,],[120,170,202,207,226,]),'FALSE':([70,90,100,101,166,],[121,171,203,208,227,]),'STRING':([81,],[150,]),'ELSE':([242,256,],[245,257,]),'ELIF':([242,],[246,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([0,],[2,]),'main_function':([0,2,],[3,9,]),'type_keyword':([0,14,15,25,27,28,30,31,33,86,87,88,104,236,237,241,248,249,254,258,],[4,17,17,17,55,55,55,55,55,55,55,55,17,55,55,55,55,55,55,55,]),'argument_list':([14,15,25,104,],[18,21,29,215,]),'argument':([14,15,25,104,],[19,19,19,19,]),'statement_list':([27,28,30,33,],[32,64,65,68,]),'statement':([27,28,30,33,88,236,237,248,254,258,],[33,33,33,33,165,239,240,250,255,259,]),'expression_statement':([27,28,30,33,88,236,237,248,254,258,],[34,34,34,34,34,34,34,34,34,34,]),'control_statement':([27,28,30,33,88,236,237,248,254,258,],[35,35,35,35,35,35,35,35,35,35,]),'return_statement':([27,28,30,33,88,236,237,248,254,258,],[36,36,36,36,36,36,36,36,36,36,]),'print_statement':([27,28,30,33,88,236,237,248,254,258,],[37,37,37,37,37,37,37,37,37,37,]),'expression':([27,28,30,31,33,86,87,88,236,237,241,248,249,254,258,],[38,38,38,66,38,163,164,38,38,38,244,38,251,38,38,]),'if_statement':([27,28,30,33,88,236,237,248,254,258,],[39,39,39,39,39,39,39,39,39,39,]),'while_statement':([27,28,30,33,88,236,237,248,254,258,],[40,40,40,40,40,40,40,40,40,40,]),'do_while_statement':([27,28,30,33,88,236,237,248,254,258,],[41,41,41,41,41,41,41,41,41,41,]),'assignment_expression':([27,28,30,31,33,86,87,88,236,237,241,248,249,254,258,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'logical_expression':([27,28,30,31,33,86,87,88,236,237,241,248,249,254,258,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'unary_expression':([27,28,30,31,33,86,87,88,236,237,241,248,249,254,258,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'arithmetic_expression':([27,28,30,31,33,86,87,88,90,166,236,237,241,248,249,254,258,],[49,49,49,49,49,49,49,49,172,228,49,49,49,49,49,49,49,]),'relational_expression':([27,28,30,31,33,63,82,83,84,85,86,87,88,102,103,236,237,241,248,249,254,258,],[50,50,50,50,50,113,151,154,159,162,50,50,50,210,213,50,50,50,50,50,50,50,]),'equality_expression':([27,28,30,31,33,63,82,83,84,85,86,87,88,102,103,236,237,241,248,249,254,258,],[51,51,51,51,51,112,153,156,157,160,51,51,51,211,214,51,51,51,51,51,51,51,]),'function_call':([27,28,30,31,33,86,87,88,90,166,236,237,241,248,249,254,258,],[57,57,57,57,57,57,57,57,173,229,57,57,57,57,57,57,57,]),'logical_or_expression':([27,28,30,31,33,63,86,87,88,236,237,241,248,249,254,258,],[58,58,58,58,58,110,58,58,58,58,58,58,58,58,58,58,]),'logical_and_expression':([27,28,30,31,33,63,86,87,88,236,237,241,248,249,254,258,],[59,59,59,59,59,109,59,59,59,59,59,59,59,59,59,59,]),'logical_not_expression':([27,28,30,31,33,86,87,88,236,237,241,248,249,254,258,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'number':([61,62,],[105,108,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function main_function','program',2,'p_program','parser.py',34),
  ('program -> main_function','program',1,'p_program','parser.py',35),
  ('main_function -> TYPE_INT MAIN LPAREN RPAREN LBRACE statement_list RBRACE','main_function',7,'p_main_function','parser.py',45),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',52),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','parser.py',53),
  ('statement -> expression_statement','statement',1,'p_statement','parser.py',63),
  ('statement -> control_statement','statement',1,'p_statement','parser.py',64),
  ('statement -> return_statement','statement',1,'p_statement','parser.py',65),
  ('statement -> print_statement','statement',1,'p_statement','parser.py',66),
  ('expression_statement -> expression SEMICOLON','expression_statement',2,'p_expression_statement','parser.py',73),
  ('control_statement -> if_statement','control_statement',1,'p_control_statement','parser.py',80),
  ('control_statement -> while_statement','control_statement',1,'p_control_statement','parser.py',81),
  ('control_statement -> do_while_statement','control_statement',1,'p_control_statement','parser.py',82),
  ('type_keyword -> TYPE_INT','type_keyword',1,'p_type_keyword','parser.py',99),
  ('type_keyword -> TYPE_BOOL','type_keyword',1,'p_type_keyword','parser.py',100),
  ('type_keyword -> TYPE_FLOAT','type_keyword',1,'p_type_keyword','parser.py',101),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statement RBRACE','if_statement',7,'p_if_statement','parser.py',108),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE','if_statement',11,'p_if_statement','parser.py',109),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statement RBRACE ELIF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE','if_statement',18,'p_if_statement','parser.py',110),
  ('while_statement -> WHILE LPAREN expression RPAREN LBRACE statement RBRACE','while_statement',7,'p_while_statement','parser.py',122),
  ('do_while_statement -> DO LBRACE statement RBRACE WHILE LPAREN expression RPAREN','do_while_statement',8,'p_do_while_statement','parser.py',128),
  ('return_statement -> RETURN LPAREN INTEGER RPAREN SEMICOLON','return_statement',5,'p_return_statement','parser.py',133),
  ('return_statement -> RETURN LPAREN FLOAT RPAREN SEMICOLON','return_statement',5,'p_return_statement','parser.py',134),
  ('return_statement -> RETURN LPAREN TRUE RPAREN SEMICOLON','return_statement',5,'p_return_statement','parser.py',135),
  ('return_statement -> RETURN LPAREN FALSE RPAREN SEMICOLON','return_statement',5,'p_return_statement','parser.py',136),
  ('print_statement -> PRINT LPAREN STRING RPAREN SEMICOLON','print_statement',5,'p_print_statement','parser.py',143),
  ('expression -> assignment_expression','expression',1,'p_expression','parser.py',150),
  ('expression -> logical_expression','expression',1,'p_expression','parser.py',151),
  ('expression -> unary_expression','expression',1,'p_expression','parser.py',152),
  ('expression -> arithmetic_expression','expression',1,'p_expression','parser.py',153),
  ('expression -> relational_expression','expression',1,'p_expression','parser.py',154),
  ('expression -> equality_expression','expression',1,'p_expression','parser.py',155),
  ('arithmetic_expression -> IDENTIFIER PLUS IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',162),
  ('arithmetic_expression -> IDENTIFIER PLUS INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',163),
  ('arithmetic_expression -> IDENTIFIER MODULUS IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',164),
  ('arithmetic_expression -> IDENTIFIER MINUS IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',165),
  ('arithmetic_expression -> IDENTIFIER MINUS INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',166),
  ('arithmetic_expression -> IDENTIFIER MINUS FLOAT','arithmetic_expression',3,'p_arithmetic_expression','parser.py',167),
  ('arithmetic_expression -> IDENTIFIER MODULUS INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',168),
  ('arithmetic_expression -> IDENTIFIER MULTIPLY IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',169),
  ('arithmetic_expression -> IDENTIFIER MULTIPLY INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',170),
  ('arithmetic_expression -> IDENTIFIER MULTIPLY FLOAT','arithmetic_expression',3,'p_arithmetic_expression','parser.py',171),
  ('arithmetic_expression -> IDENTIFIER DIVIDE IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',172),
  ('arithmetic_expression -> IDENTIFIER DIVIDE INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',173),
  ('arithmetic_expression -> IDENTIFIER DIVIDE FLOAT','arithmetic_expression',3,'p_arithmetic_expression','parser.py',174),
  ('arithmetic_expression -> INTEGER PLUS INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',175),
  ('arithmetic_expression -> INTEGER PLUS IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',176),
  ('arithmetic_expression -> INTEGER MODULUS IDENTIFIER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',177),
  ('arithmetic_expression -> INTEGER MODULUS INTEGER','arithmetic_expression',3,'p_arithmetic_expression','parser.py',178),
  ('assignment_expression -> type_keyword IDENTIFIER ASSIGN INTEGER','assignment_expression',4,'p_assignment_expression','parser.py',194),
  ('assignment_expression -> type_keyword IDENTIFIER ASSIGN FLOAT','assignment_expression',4,'p_assignment_expression','parser.py',195),
  ('assignment_expression -> type_keyword IDENTIFIER ASSIGN TRUE','assignment_expression',4,'p_assignment_expression','parser.py',196),
  ('assignment_expression -> type_keyword IDENTIFIER ASSIGN FALSE','assignment_expression',4,'p_assignment_expression','parser.py',197),
  ('assignment_expression -> type_keyword IDENTIFIER ASSIGN arithmetic_expression','assignment_expression',4,'p_assignment_expression','parser.py',198),
  ('assignment_expression -> type_keyword IDENTIFIER ASSIGN function_call','assignment_expression',4,'p_assignment_expression','parser.py',199),
  ('assignment_expression -> IDENTIFIER ASSIGN INTEGER','assignment_expression',3,'p_assignment_expression','parser.py',200),
  ('assignment_expression -> IDENTIFIER ASSIGN FLOAT','assignment_expression',3,'p_assignment_expression','parser.py',201),
  ('assignment_expression -> IDENTIFIER ASSIGN TRUE','assignment_expression',3,'p_assignment_expression','parser.py',202),
  ('assignment_expression -> IDENTIFIER ASSIGN FALSE','assignment_expression',3,'p_assignment_expression','parser.py',203),
  ('assignment_expression -> IDENTIFIER ASSIGN arithmetic_expression','assignment_expression',3,'p_assignment_expression','parser.py',204),
  ('assignment_expression -> IDENTIFIER ASSIGN function_call','assignment_expression',3,'p_assignment_expression','parser.py',205),
  ('logical_expression -> logical_or_expression','logical_expression',1,'p_logical_expression','parser.py',220),
  ('logical_expression -> logical_and_expression','logical_expression',1,'p_logical_expression','parser.py',221),
  ('logical_expression -> logical_not_expression','logical_expression',1,'p_logical_expression','parser.py',222),
  ('logical_or_expression -> IDENTIFIER LOGICAL_OR IDENTIFIER','logical_or_expression',3,'p_logical_or_expression','parser.py',229),
  ('logical_or_expression -> IDENTIFIER LOGICAL_OR relational_expression','logical_or_expression',3,'p_logical_or_expression','parser.py',230),
  ('logical_or_expression -> IDENTIFIER LOGICAL_OR equality_expression','logical_or_expression',3,'p_logical_or_expression','parser.py',231),
  ('logical_or_expression -> relational_expression LOGICAL_OR IDENTIFIER','logical_or_expression',3,'p_logical_or_expression','parser.py',232),
  ('logical_or_expression -> relational_expression LOGICAL_OR relational_expression','logical_or_expression',3,'p_logical_or_expression','parser.py',233),
  ('logical_or_expression -> relational_expression LOGICAL_OR equality_expression','logical_or_expression',3,'p_logical_or_expression','parser.py',234),
  ('logical_or_expression -> equality_expression LOGICAL_OR IDENTIFIER','logical_or_expression',3,'p_logical_or_expression','parser.py',235),
  ('logical_or_expression -> equality_expression LOGICAL_OR relational_expression','logical_or_expression',3,'p_logical_or_expression','parser.py',236),
  ('logical_or_expression -> equality_expression LOGICAL_OR equality_expression','logical_or_expression',3,'p_logical_or_expression','parser.py',237),
  ('logical_and_expression -> IDENTIFIER LOGICAL_AND IDENTIFIER','logical_and_expression',3,'p_logical_and_expression','parser.py',245),
  ('logical_and_expression -> IDENTIFIER LOGICAL_AND relational_expression','logical_and_expression',3,'p_logical_and_expression','parser.py',246),
  ('logical_and_expression -> IDENTIFIER LOGICAL_AND equality_expression','logical_and_expression',3,'p_logical_and_expression','parser.py',247),
  ('logical_and_expression -> relational_expression LOGICAL_AND IDENTIFIER','logical_and_expression',3,'p_logical_and_expression','parser.py',248),
  ('logical_and_expression -> relational_expression LOGICAL_AND relational_expression','logical_and_expression',3,'p_logical_and_expression','parser.py',249),
  ('logical_and_expression -> relational_expression LOGICAL_AND equality_expression','logical_and_expression',3,'p_logical_and_expression','parser.py',250),
  ('logical_and_expression -> equality_expression LOGICAL_AND IDENTIFIER','logical_and_expression',3,'p_logical_and_expression','parser.py',251),
  ('logical_and_expression -> equality_expression LOGICAL_AND relational_expression','logical_and_expression',3,'p_logical_and_expression','parser.py',252),
  ('logical_and_expression -> equality_expression LOGICAL_AND equality_expression','logical_and_expression',3,'p_logical_and_expression','parser.py',253),
  ('logical_not_expression -> LOGICAL_NOT logical_and_expression','logical_not_expression',2,'p_logical_not_expression','parser.py',261),
  ('logical_not_expression -> LOGICAL_NOT logical_or_expression','logical_not_expression',2,'p_logical_not_expression','parser.py',262),
  ('logical_not_expression -> LOGICAL_NOT IDENTIFIER','logical_not_expression',2,'p_logical_not_expression','parser.py',263),
  ('logical_not_expression -> LOGICAL_NOT equality_expression','logical_not_expression',2,'p_logical_not_expression','parser.py',264),
  ('logical_not_expression -> LOGICAL_NOT relational_expression','logical_not_expression',2,'p_logical_not_expression','parser.py',265),
  ('equality_expression -> IDENTIFIER EQUALS IDENTIFIER','equality_expression',3,'p_equality_expression','parser.py',273),
  ('equality_expression -> IDENTIFIER EQUALS INTEGER','equality_expression',3,'p_equality_expression','parser.py',274),
  ('equality_expression -> IDENTIFIER EQUALS FLOAT','equality_expression',3,'p_equality_expression','parser.py',275),
  ('equality_expression -> IDENTIFIER EQUALS TRUE','equality_expression',3,'p_equality_expression','parser.py',276),
  ('equality_expression -> IDENTIFIER EQUALS FALSE','equality_expression',3,'p_equality_expression','parser.py',277),
  ('equality_expression -> IDENTIFIER NOT_EQUALS IDENTIFIER','equality_expression',3,'p_equality_expression','parser.py',278),
  ('equality_expression -> IDENTIFIER NOT_EQUALS INTEGER','equality_expression',3,'p_equality_expression','parser.py',279),
  ('equality_expression -> IDENTIFIER NOT_EQUALS FLOAT','equality_expression',3,'p_equality_expression','parser.py',280),
  ('equality_expression -> IDENTIFIER NOT_EQUALS TRUE','equality_expression',3,'p_equality_expression','parser.py',281),
  ('equality_expression -> IDENTIFIER NOT_EQUALS FALSE','equality_expression',3,'p_equality_expression','parser.py',282),
  ('relational_expression -> IDENTIFIER GREATER_THAN IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',292),
  ('relational_expression -> IDENTIFIER GREATER_THAN INTEGER','relational_expression',3,'p_relational_expression','parser.py',293),
  ('relational_expression -> IDENTIFIER GREATER_THAN FLOAT','relational_expression',3,'p_relational_expression','parser.py',294),
  ('relational_expression -> IDENTIFIER LESS_THAN IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',295),
  ('relational_expression -> IDENTIFIER LESS_THAN INTEGER','relational_expression',3,'p_relational_expression','parser.py',296),
  ('relational_expression -> IDENTIFIER LESS_THAN FLOAT','relational_expression',3,'p_relational_expression','parser.py',297),
  ('relational_expression -> IDENTIFIER LESS_THAN_OR_EQUAL IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',298),
  ('relational_expression -> IDENTIFIER LESS_THAN_OR_EQUAL INTEGER','relational_expression',3,'p_relational_expression','parser.py',299),
  ('relational_expression -> IDENTIFIER LESS_THAN_OR_EQUAL FLOAT','relational_expression',3,'p_relational_expression','parser.py',300),
  ('relational_expression -> IDENTIFIER GREATER_THAN_OR_EQUAL IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',301),
  ('relational_expression -> IDENTIFIER GREATER_THAN_OR_EQUAL INTEGER','relational_expression',3,'p_relational_expression','parser.py',302),
  ('relational_expression -> IDENTIFIER GREATER_THAN_OR_EQUAL FLOAT','relational_expression',3,'p_relational_expression','parser.py',303),
  ('relational_expression -> INTEGER GREATER_THAN IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',304),
  ('relational_expression -> INTEGER GREATER_THAN INTEGER','relational_expression',3,'p_relational_expression','parser.py',305),
  ('relational_expression -> INTEGER GREATER_THAN FLOAT','relational_expression',3,'p_relational_expression','parser.py',306),
  ('relational_expression -> INTEGER LESS_THAN IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',307),
  ('relational_expression -> INTEGER LESS_THAN INTEGER','relational_expression',3,'p_relational_expression','parser.py',308),
  ('relational_expression -> INTEGER LESS_THAN FLOAT','relational_expression',3,'p_relational_expression','parser.py',309),
  ('relational_expression -> INTEGER LESS_THAN_OR_EQUAL IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',310),
  ('relational_expression -> INTEGER LESS_THAN_OR_EQUAL INTEGER','relational_expression',3,'p_relational_expression','parser.py',311),
  ('relational_expression -> INTEGER LESS_THAN_OR_EQUAL FLOAT','relational_expression',3,'p_relational_expression','parser.py',312),
  ('relational_expression -> INTEGER GREATER_THAN_OR_EQUAL IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',313),
  ('relational_expression -> INTEGER GREATER_THAN_OR_EQUAL INTEGER','relational_expression',3,'p_relational_expression','parser.py',314),
  ('relational_expression -> INTEGER GREATER_THAN_OR_EQUAL FLOAT','relational_expression',3,'p_relational_expression','parser.py',315),
  ('relational_expression -> FLOAT GREATER_THAN IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',316),
  ('relational_expression -> FLOAT GREATER_THAN INTEGER','relational_expression',3,'p_relational_expression','parser.py',317),
  ('relational_expression -> FLOAT GREATER_THAN FLOAT','relational_expression',3,'p_relational_expression','parser.py',318),
  ('relational_expression -> FLOAT LESS_THAN IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',319),
  ('relational_expression -> FLOAT LESS_THAN INTEGER','relational_expression',3,'p_relational_expression','parser.py',320),
  ('relational_expression -> FLOAT LESS_THAN FLOAT','relational_expression',3,'p_relational_expression','parser.py',321),
  ('relational_expression -> FLOAT LESS_THAN_OR_EQUAL IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',322),
  ('relational_expression -> FLOAT LESS_THAN_OR_EQUAL INTEGER','relational_expression',3,'p_relational_expression','parser.py',323),
  ('relational_expression -> FLOAT LESS_THAN_OR_EQUAL FLOAT','relational_expression',3,'p_relational_expression','parser.py',324),
  ('relational_expression -> FLOAT GREATER_THAN_OR_EQUAL IDENTIFIER','relational_expression',3,'p_relational_expression','parser.py',325),
  ('relational_expression -> FLOAT GREATER_THAN_OR_EQUAL INTEGER','relational_expression',3,'p_relational_expression','parser.py',326),
  ('relational_expression -> FLOAT GREATER_THAN_OR_EQUAL FLOAT','relational_expression',3,'p_relational_expression','parser.py',327),
  ('unary_expression -> MINUS number','unary_expression',2,'p_unary_expression','parser.py',342),
  ('unary_expression -> PLUS number','unary_expression',2,'p_unary_expression','parser.py',343),
  ('unary_expression -> function_call','unary_expression',1,'p_unary_expression','parser.py',344),
  ('unary_expression -> IDENTIFIER','unary_expression',1,'p_unary_expression','parser.py',345),
  ('unary_expression -> LPAREN expression RPAREN','unary_expression',3,'p_unary_expression','parser.py',346),
  ('function -> type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE','function',8,'p_function','parser.py',365),
  ('function -> VOID IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE','function',8,'p_function','parser.py',366),
  ('function_call -> IDENTIFIER LPAREN argument_list RPAREN','function_call',4,'p_function_call','parser.py',373),
  ('argument_list -> argument','argument_list',1,'p_argument_list','parser.py',389),
  ('argument_list -> argument COMMA argument_list','argument_list',3,'p_argument_list','parser.py',390),
  ('argument -> type_keyword IDENTIFIER','argument',2,'p_argument','parser.py',400),
  ('number -> INTEGER','number',1,'p_number','parser.py',406),
  ('number -> FLOAT','number',1,'p_number','parser.py',407),
]