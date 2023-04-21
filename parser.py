import ply.yacc as yacc
import lexer

tokens = lexer.tokens
token_string = lexer.token_string
print('\nOutput string from the lexer is: ')
print(token_string)
print('\n')

# NOTE:
# The tokens that are in capital are already defined in the token list and hence don't need rules
# The tokens/terminal symbols are imported as list called tokens
# The output of the lexer is also imported to the parser

# Define the precedence and associativity of the operators
precedence = (
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_AND'),
    ('left', 'EQUALS', 'NOT_EQUALS'),
    ('left', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULUS'),
    ('right', 'LOGICAL_NOT'),
    ('nonassoc', 'EQUALS'),
)


# Define the grammar rules
def p_program(p):
    '''
    program : function main_function
            | main_function
    '''
    if len(p) == 3:
        p[0] = ('program', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('program', p[1])


def p_main_function(p):
    '''
    main_function : TYPE_INT MAIN LPAREN RPAREN LBRACE statement_list RETURN SEMICOLON RBRACE
    '''
    p[0] = ('main_function', p[6])


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement statement_list
    '''
    if len(p) == 3:
        p[0] = ('statement_list', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('statement', p[1])


def p_statement(p):
    '''
    statement : expression_statement
              | control_statement
              | return_statement
              | print_statement
    '''
    p[0] = ('statement', p[1])


def p_expression_statement(p):
    '''
    expression_statement : expression SEMICOLON
    '''
    p[0] = ('expression_statement', p[1])


def p_control_statement(p):
    '''
    control_statement : if_statement
                      | while_statement
                      | do_while_statement
    '''
    p[0] = ('control_statement', p[1])


def p_control_keyword(p):
    '''
    control_keyword : WHILE
                    | IF
                    | ELSE
                    | DO
    '''
    p[0] = ('control_keyword', p[1])


def p_type_keyword(p):
    '''
    type_keyword : TYPE_INT
                 | TYPE_BOOL
                 | TYPE_FLOAT
    '''
    p[0] = ('type_keyword', p[1])


def p_if_statement(p):
    '''
    if_statement : IF LPAREN expression RPAREN LBRACE statement RBRACE
                 | IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
                 | IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE_IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
    '''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    elif len(p) == 12:
        p[0] = ('if_else', p[3], p[6], p[10])
    elif len(p) == 19:
        p[0] = ('if_elseif_else', p[3], p[6], p[10], p[13], p[17])


def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE
    '''
    p[0] = ('while_statement', p[3], p[6])


def p_do_while_statement(p):
    '''do_while_statement : DO LBRACE statement RBRACE WHILE LPAREN expression RPAREN'''
    p[0] = ('do_while_statement', p[3], p[6])


def p_return_statement(p):
    '''return_statement : RETURN LPAREN expression RPAREN SEMICOLON'''
    p[0] = ('return_statement', p[3])


def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN STRING RPAREN SEMICOLON
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
    arithmetic_expression   : IDENTIFIER PLUS IDENTIFIER
                            | IDENTIFIER PLUS INTEGER
                            | IDENTIFIER MINUS IDENTIFIER
                            | IDENTIFIER MINUS INTEGER
                            | IDENTIFIER MINUS FLOAT
                            | IDENTIFIER MULTIPLY IDENTIFIER
                            | IDENTIFIER MULTIPLY INTEGER
                            | IDENTIFIER MULTIPLY FLOAT
                            | IDENTIFIER DIVIDE IDENTIFIER
                            | IDENTIFIER DIVIDE INTEGER
                            | IDENTIFIER DIVIDE FLOAT
                            | INTEGER PLUS INTEGER
                            | INTEGER PLUS IDENTIFIER

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
    assignment_expression : type_keyword IDENTIFIER ASSIGN INTEGER
                          | type_keyword IDENTIFIER ASSIGN FLOAT
                          | type_keyword IDENTIFIER ASSIGN TRUE
                          | type_keyword IDENTIFIER ASSIGN FALSE
                          | type_keyword IDENTIFIER ASSIGN arithmetic_expression
                          | type_keyword IDENTIFIER ASSIGN function_call
                          | IDENTIFIER ASSIGN INTEGER
                          | IDENTIFIER ASSIGN FLOAT
                          | IDENTIFIER ASSIGN TRUE
                          | IDENTIFIER ASSIGN FALSE
                          | IDENTIFIER ASSIGN arithmetic_expression
                          | IDENTIFIER ASSIGN function_call

    '''
    if p[3] == '=':
        p[0] = p[1], p[2], = p[4]
    else:
        p[0] = p[1] = p[3]

def p_logical_expression(p):
    '''
    logical_expression : logical_or_expression
                       | logical_and_expression
                       | logical_not_expression
    '''
    p[0] = ('logical_expression', p[1])


def p_logical_or_expression(p):
    '''
    logical_or_expression   : IDENTIFIER LOGICAL_OR IDENTIFIER
                            | IDENTIFIER LOGICAL_OR relational_expression
                            | IDENTIFIER LOGICAL_OR equality_expression
                            | relational_expression LOGICAL_OR IDENTIFIER
                            | relational_expression LOGICAL_OR relational_expression
                            | relational_expression LOGICAL_OR equality_expression
                            | equality_expression LOGICAL_OR IDENTIFIER
                            | equality_expression LOGICAL_OR relational_expression
                            | equality_expression LOGICAL_OR equality_expression
    '''
    p[0] = p[1] or p[3]


def p_logical_and_expression(p):
    '''
    logical_and_expression : IDENTIFIER LOGICAL_AND IDENTIFIER
                           | IDENTIFIER LOGICAL_AND relational_expression
                           | IDENTIFIER LOGICAL_AND equality_expression
                           | relational_expression LOGICAL_AND IDENTIFIER
                           | relational_expression LOGICAL_AND relational_expression
                           | relational_expression LOGICAL_AND equality_expression
                           | equality_expression LOGICAL_AND IDENTIFIER
                           | equality_expression LOGICAL_AND relational_expression
                           | equality_expression LOGICAL_AND equality_expression

    '''
    p[0] = p[1] and p[3]


def p_logical_not(p):
    '''logical_not_expression   : LOGICAL_NOT logical_and_expression
                                | LOGICAL_NOT logical_or_expression
                                | LOGICAL_NOT IDENTIFIER
                                | LOGICAL_NOT equality_expression
                                | LOGICAL_NOT relational_expression
    '''

    p[0] = not (p[2])


def p_equality_expression(p):
    '''equality_expression : IDENTIFIER EQUALS IDENTIFIER
                           | IDENTIFIER EQUALS INTEGER
                           | IDENTIFIER EQUALS FLOAT
                           | IDENTIFIER EQUALS TRUE
                           | IDENTIFIER EQUALS FALSE
                           | IDENTIFIER NOT_EQUALS IDENTIFIER
                           | IDENTIFIER NOT_EQUALS INTEGER
                           | IDENTIFIER NOT_EQUALS FLOAT
                           | IDENTIFIER NOT_EQUALS TRUE
                           | IDENTIFIER NOT_EQUALS FALSE
    '''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]


def p_relational_expression(p):
    ''' relational_expression   : IDENTIFIER GREATER_THAN IDENTIFIER
                                | IDENTIFIER GREATER_THAN INTEGER
                                | IDENTIFIER GREATER_THAN FLOAT
                                | IDENTIFIER LESS_THAN_OR_EQUAL IDENTIFIER
                                | IDENTIFIER LESS_THAN_OR_EQUAL INTEGER
                                | IDENTIFIER LESS_THAN_OR_EQUAL FLOAT
                                | IDENTIFIER GREATER_THAN_OR_EQUAL IDENTIFIER
                                | IDENTIFIER GREATER_THAN_OR_EQUAL INTEGER
                                | IDENTIFIER GREATER_THAN_OR_EQUAL FLOAT
                                | INTEGER GREATER_THAN IDENTIFIER
                                | INTEGER GREATER_THAN INTEGER
                                | INTEGER GREATER_THAN FLOAT
                                | INTEGER LESS_THAN_OR_EQUAL IDENTIFIER
                                | INTEGER LESS_THAN_OR_EQUAL INTEGER
                                | INTEGER LESS_THAN_OR_EQUAL FLOAT
                                | INTEGER GREATER_THAN_OR_EQUAL IDENTIFIER
                                | INTEGER GREATER_THAN_OR_EQUAL INTEGER
                                | INTEGER GREATER_THAN_OR_EQUAL FLOAT
                                | FLOAT GREATER_THAN IDENTIFIER
                                | FLOAT GREATER_THAN INTEGER
                                | FLOAT GREATER_THAN FLOAT
                                | FLOAT LESS_THAN_OR_EQUAL IDENTIFIER
                                | FLOAT LESS_THAN_OR_EQUAL INTEGER
                                | FLOAT LESS_THAN_OR_EQUAL FLOAT
                                | FLOAT GREATER_THAN_OR_EQUAL IDENTIFIER
                                | FLOAT GREATER_THAN_OR_EQUAL INTEGER
                                | FLOAT GREATER_THAN_OR_EQUAL FLOAT
    '''
    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>+':
        p[0] = p[1] > + p[3]


def p_unary_expression(p):
    '''unary_expression    : primary_expression
                            | MINUS primary_expression
                            | PLUS primary_expression'''

    if p[1] == '-':
        p[0] = - p[2]
    elif p[1] == '+':
        p[0] = + p[2]
    else:
        p[0] = p[1]


def p_primary_expression(p):
    '''primary_expression   : IDENTIFIER
                            | number
                            | LPAREN expression RPAREN
                            | function_call '''
    if p[1] == '(':
        p[0] = (p[1])
    else:
        p[0] = p[1]


def p_function(p):
    '''function : type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = p[1], p[2], (p[4]), {p[7]}


def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN argument_list RPAREN '''
    p[0] = p[1](p[3])


def p_argument_list(p):
    '''argument_list : type_keyword expression COMMA type_keyword expression
                     | type_keyword expression
    '''
    p[0] = p[1], p[2], p[3], p[4]


def p_number(p):
    '''number   : INTEGER
                | FLOAT'''
    p[0] = p[1]


def p_error(p):
    print('Syntax error at {}'.format(p.value))


# create a parser instance
parser = yacc.yacc()
# parser = yacc.yacc(debug=True, write_tables=False, optimize=False, start='program', lexer=lexer)


# call the parse method to parse the token string
ast = parser.parse(token_string)
print(ast)