def p_right_brace(p):
    '''right_brace : '}' '''
    # Perform any necessary syntax checks
    # Close the block of code
    p[0] = None

def p_left_paren(p):
    '''left_paren : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_right_paren(p):
    '''right_paren : expression RPAREN'''
    p[0] = p[1]

def p_left_bracket(p):
    '''left_bracket : LBRACKET expression RBRACKET'''
    p[0] = p[2]

def p_right_bracket(p):
    '''right_bracket : expression RBRACKET'''
    p[0] = p[1]

def p_minus(p):
    '''minus : MINUS expression %prec UMINUS'''
    p[0] = -p[2]

def p_plus(p):
    '''plus : expression PLUS expression'''
    p[0] = p[1] + p[3]

def p_multiply(p):
    '''multiply : expression TIMES expression'''
    p[0] = p[1] * p[3]

def p_divide(p):
    '''divide : expression DIVIDE expression'''
    if p[3] == 0:
        raise ZeroDivisionError("division by zero")
    p[0] = p[1] / p[3]

def p_backslash(p):
    '''backslash : expression BACKSLASH expression'''
    p[0] = p[1] // p[3]  # floor division operator

def p_modulus(p):
    '''modulus : expression MODULUS expression'''
    p[0] = p[1] % p[3]   # modulo operator

def p_equality_expression(p):
    '''equality expression : relational_expression equals relational_expression
                           | relational_expression not_equals relational_expression'''
    if p[2] == EQUALS:
        p[0] = p[1] == p[3]
    elif p[2] == NOT_EQUALS:
        p[0] = p[1] != p[3]

def p_equality_expression(p):
    '''equality expression : relational_expression equals relational_expression
                           | relational_expression not_equals relational_expression'''
    if p[2] == '==':
        p[0] =  p[1] == p[3] 
    elif p[2] == '!=':
        p[0] =  p[1] != p[3]

def p_relational_expression(p):
    '''relational_expression : additive_expression
                             | additive_expression less_than additive_expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] < p[3]

def p_relational_expression(p):
    '''relational_expression : additive_expression
                              | relational_expression less_than additive_expression
                              | relational_expression greater_than additive_expression
                              | relational_expression less_than_or_equal additive_expression'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]

def p_equality_expression(p):
    '''equality_expression : relational_expression equals relational_expression
                           | relational_expression not_equals relational_expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3] 
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

def p_logical_and_expression(p):
    '''logical_and_expression : equality_expression logical_and equality_expression'''
    p[0] = p[1] and p[3]
def p_equality_expression(p):
    '''equality expression : relational_expression equals relational_expression
                           | relational_expression not_equals relational_expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                             | logical_or_expression logical_or logical_and_expression'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] or p[3]

def p_logical_not_expression(p):
    '''logical_not_expression : logical_not unary_expression'''
    p[0] = not p[2]

def p_assignment_expression(p):
    '''assignment_expression : unary_expression assign assignment_expression
                             | conditional_expression'''
    if len(p) == 4:
        p[1] = p[3]
    p[0] = p[1]

