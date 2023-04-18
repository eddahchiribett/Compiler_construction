
def p_logical_not(p):
    '''logical_not_expression : logical_not logical_and_expression
                              | logical_not logical_or_expression'''
    p[0] = not ( p[2] )

def p_equality_expression(p):
    '''equality expression : relational_expression equals relational_expression
                           | relational_expression not_equals relational_expression'''
    if p[2]== '==':
        p[0] =  p[1] == p[3] 
    elif p[2] == '!=':
          p[0] =  p[1] != p[3] 

def p_relational_expression(p):
    '''relational_expression : additive_expression less_than additive_expression
                             | additive_expression greater_than additive_expression 
                             | additive_expression less_than_or_equal additive_expression 
                             | additive_expression greater_than_or_equal additive_expression'''
    if p[2]== '<':
        p[0] = p[1] < p[3] 
    elif p[2] == '>':
          p[0] =  p[1] > p[3] 
    elif p[2] == '<=':
          p[0] =  p[1] <= p[3]
    elif p[2] == '>+':
          p[0] = p[1] >+ p[3]     

def p_additive_expression(p):
    '''additive_expression : multiplicative_expression plus multiplicative_expression 
                           | multiplicative_expression minus multiplicative_expression '''
        #didn't add repeating section of multiplicative , requires grammar rework
        #maybe just have two-term expressions
    if p[2]== '+':
        p[0] =  p[1] + p[3] 
    elif p[2] == '-':
          p[0] =  p[1] - p[3] 

def p_multiplicative_expression(p):
    '''multiplicative_expression    : unary_expression multiply unary_expression 
                                    | unary_expression divide unary_expression>'''
    #didn't add repeating section of unary , requires grammar rework
    #again, maybe just have two-term expressions
    if p[2]== '*':
        p[0] = ( p[1] * p[3] )
    elif p[2] == '/':
          p[0] = ( p[1] / p[3] )

def p_unary_expression(p):
    '''<unary_expression> ::= primary_expression 
                            | minus primary_expression 
                            | plus primary_expression'''
    #maybe the plus and minus should be added at the number non-terminal 
    # instead of here since this can give us negative function calls
    if p[1]== '-':
        p[0] =  - p[2] 
    elif p[1] == '+':
        p[0] = + p[2] 
    else:
        p[0]= p[1]  

def p_primary_expression(p):
    '''<primary_expression> : identifier 
                            | number 
                            | left_paren expression right_paren
                            | function_call '''
    if p[1] =='(':
        p[0] = ( p[1] )
    else:
         p[0]= p[1]

def p_function(p):
    '''function : type_keyword identifier left_paren argument_list right_paren left_brace statement_list right_brace'''
    #not really sure how commas interact here
    p[0] = p[1],p[2], (p[4]), {p[7]}

def p_function_call(p):
    '''function_call : identifier left_paren argument_list right_paren'''
    p[0]= p[1](p[3])


def p_argument_list(p):
    '''argument_list : type_keyword expression  '''
    #not sure abt recursion, also think this should be unary expression
    p[0] = p[1],p[2]

def p_number(p):
    '''number   : integer
                | float'''
    p[0]=p[1]