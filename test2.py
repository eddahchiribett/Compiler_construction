

# logical_not_expression  : LOGICAL_NOT logical_and_expression 
#                         | LOGICAL_NOT logical_or_expression 
#                         | LOGICAL_NOT (IDENTIFIER | equality_expression | relational_expression )
#                         ;
                        
                        
# equality_expression : IDENTIFIER (EQUALS | NOT_EQUALS ) (IDENTIFIER| INT | FLOAT| TRUE | FALSE)
#                     ;
# relational_expression   : (IDENTIFIER| INT | FLOAT) (LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL) ( IDENTIFIER| INT | FLOAT)
#                         ;

# unary_expression    : primary_expression 
#                     | MINUS primary_expression 
#                     | PLUS primary_expression
#                     ;
# primary_expression  : IDENTIFIER 
#                     | number 
#                     | LPAREN expression RPAREN 
#                     | function_call
#                     ;
# function : type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE;
# function_call : IDENTIFIER LPAREN argument_list RPAREN;
# argument_list : type_keyword expression (COMMA type_keyword expression)*;
# number  : INT
#         | FLOAT;

        
def p_logical_not(p):
    '''logical_not_expression   : LOGICAL_NOT logical_and_expression 
                                | LOGICAL_NOT logical_or_expression 
                                | LOGICAL_NOT (IDENTIFIER | equality_expression | relational_expression )'''
                        ;
    p[0] = not ( p[2] )

def p_equality_expression(p):
    '''equality_expression : IDENTIFIER (EQUALS | NOT_EQUALS ) (IDENTIFIER| INT | FLOAT| TRUE | FALSE)'''
    if p[2]== '==':
        p[0] =  p[1] == p[3] 
    elif p[2] == '!=':
          p[0] =  p[1] != p[3] 

def p_relational_expression(p):
    ''' relational_expression   : (IDENTIFIER | INT | FLOAT) (LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL) (IDENTIFIER | INT | FLOAT)'''
    if p[2]== '<':
        p[0] = p[1] < p[3] 
    elif p[2] == '>':
          p[0] =  p[1] > p[3] 
    elif p[2] == '<=':
          p[0] =  p[1] <= p[3]
    elif p[2] == '>+':
          p[0] = p[1] >+ p[3]     


def p_unary_expression(p):
    '''unary_expression    : primary_expression 
                            | MINUS primary_expression 
                            | PLUS primary_expression'''

    if p[1]== '-':
        p[0] =  - p[2] 
    elif p[1] == '+':
        p[0] = + p[2] 
    else:
        p[0]= p[1]  

def p_primary_expression(p):
    '''primary_expression   : IDENTIFIER
                            | number 
                            | LPAREN expression RPAREN
                            | function_call '''
    if p[1] =='(':
        p[0] = ( p[1] )
    else:
         p[0]= p[1]

def p_function(p):
    '''function : type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = p[1],p[2], (p[4]), {p[7]}

def p_function_call(p):
    '''function_call :IDENTIFIER LPAREN argument_list RPAREN '''
    p[0]= p[1](p[3])


def p_argument_list(p):
    '''argument_list : type_keyword expression (COMMA type_keyword expression)*  '''
    p[0] = p[1],p[2],p[3],p[4]

def p_number(p):
    '''number   : INT
                | FLOAT'''
    p[0]=p[1]