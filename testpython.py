while_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE;

do_while_statement : DO LBRACE statement RBRACE WHILE LPAREN expression RPAREN;

for_statement : FOR LPAREN assignment_expression logical_expression assignment_expression RPAREN  LBRACE statement_list RBRACE;

return_statement : RETURN LPAREN expression RPAREN SEMICOLON;
print_statement : PRINT LPAREN STRING RPAREN SEMICOLON ;

expression  : assignment_expression 
            | logical_expression
            | unary_expression
            | arithmetic_expression
            | relational_expression
            | equality_expression
            ;
            
arithmetic_expression   : (IDENTIFIER| INT | FLOAT) (PLUS | MINUS | MULTIPLY| DIVIDE) ( IDENTIFIER| INT | FLOAT);
assignment_expression   :type_keyword IDENTIFIER ASSIGN INT
                        |type_keyword IDENTIFIER ASSIGN FLOAT
                        |type_keyword IDENTIFIER ASSIGN TRUE
                        |type_keyword IDENTIFIER ASSIGN FALSE
                        |type_keyword IDENTIFIER ASSIGN arithmetic_expression
                        |type_keyword IDENTIFIER ASSIGN function_call 
                        | IDENTIFIER ASSIGN INT
                        | IDENTIFIER ASSIGN FLOAT
                        | IDENTIFIER ASSIGN TRUE
                        | IDENTIFIER ASSIGN FALSE
                        | IDENTIFIER ASSIGN arithmetic_expression
                        | IDENTIFIER ASSIGN function_call
                       ;



def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE stat RBRACE'''
    while p[3]:
        p[6]


def p_do_while_statement(p):
    '''do_while_statement : DO LBRACE statement RBRACE WHILE LPAREN expression RPAREN SEMI'''
    while True:
        p[3]
        if not p[7]:
            break

def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment_expression logical_expression SEMI increment_expression RPAREN LBRACE statement RBRACE'''
    p[2]
    while p[3]:
        p[8]
        p[5]


def p_return_statement(p):
    '''return_statement : RETURN LPAREN expression RPAREN SEMICOLON'''
    p[0] = p[3]


def p_print_statement(p):
    '''print_statement : PRINT LPAREN STRING RPAREN SEMICOLON'''
    print(p[3])


def p_expression(p):
    '''expression : assignment_expression
                  | logical_expression
                  | unary_expression
                  | arithmetic_expression
                  | relational_expression
                  | equality_expression'''
    p[0] = p[1]



def p_arithmetic_expression(p):
    '''arithmetic_expression : (IDENTIFIER | INT | FLOAT) (PLUS | MINUS | MULTIPLY | DIVIDE) (IDENTIFIER | INT | FLOAT)'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_assignment_expression(p):
    '''assignment_expression : type_keyword IDENTIFIER ASSIGN INT
                             | type_keyword IDENTIFIER ASSIGN FLOAT
                             | type_keyword IDENTIFIER ASSIGN TRUE
                             | type_keyword IDENTIFIER ASSIGN FALSE
                             | type_keyword IDENTIFIER ASSIGN arithmetic_expression
                             | type_keyword IDENTIFIER ASSIGN function_call
                             | IDENTIFIER ASSIGN INT
                             | IDENTIFIER ASSIGN FLOAT
                             | IDENTIFIER ASSIGN TRUE
                             | IDENTIFIER ASSIGN FALSE
                             | IDENTIFIER ASSIGN arithmetic_expression
                             | IDENTIFIER ASSIGN function_call
                             '''
    if len(p) == 4:
        # Simple assignment to a variable
        p[0] = p[3]
    else:
        # Declaration and assignment of a variable with a type keyword
        p[0] = (p[1], p[2], p[4])
