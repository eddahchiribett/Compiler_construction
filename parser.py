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
                    | FOR
    '''
    p[0] = ('control_keyword', p[1])


def p_type_keyword(p):
    '''
    type_keyword : TYPE_INT
                 | TYPE_BOOL
                 | TYPE_FLOAT
    '''
    p[0] = ('type_keyword', p[1])


def if_statement(p):
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


def while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE
    '''
    p[0] = ('while_statement', p[3], p[6])


def p_error(p):
    print('Syntax error at {}'.format(p.value))


# create a parser instance
parser = yacc.yacc()
# parser = yacc.yacc(debug=True, write_tables=False, optimize=False, start='program', lexer=lexer)


# call the parse method to parse the token string
ast = parser.parse(token_string)
print(ast)
