def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN STRING RPAREN SEMICOLON ;
    '''
    p[0] = ('print', p[1])

def p_expression(p):
    '''
    expression  : assignment_expression
            | logical_expression
            | unary_expression
            | arithmetic_expression
            | relational_expression
            | equality_expression

    '''
    p[0] = ('expression', p[1])

def p_arithmetic_expression(p):
    '''
    arithmetic_expression   : (IDENTIFIER| INT | FLOAT) (PLUS | MINUS | MULTIPLY| DIVIDE) ( IDENTIFIER| INT | FLOAT)
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] == p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_assignment_expression(p):
    '''
    assignment_expression :type_keyword IDENTIFIER ASSIGN INT
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

    '''

def p_logical_expression(p):
    '''
    logical_expression: logical_or_expression
                    | logical_and_expression
                    | logical_not_expression
    '''
    p[0] = ('logical_expression', p[1])

def p_logical_or_expression(p):
    '''
    logical_or_expression   : (IDENTIFIER| relational_expression | equality_expression ) LOGICAL_OR (IDENTIFIER | relational_expression | equality_expression )
    '''
    p[0] = p[1] or p[3]

def p_logical_and_expression(p):
    '''
    logical_and_expression : (IDENTIFIER| relational_expression | equality_expression ) LOGICAL_AND (IDENTIFIER | relational_expression | equality_expression )
    '''
    p[0] = p[1] and p[3]




