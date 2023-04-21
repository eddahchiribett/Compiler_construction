import ply.yacc as yacc
import lexer

tokens = lexer.tokens
token_lst = lexer.token_list
token_list = ' '.join(token_lst)
# print(token_list)

# NOTE:-
# The tokens that are in capital are already defined in the token list and hence don't need rules
# The rules can still be created for them though with changes to this file
# The grammar may also need rework or complete replacement

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
    '''program : function main_function
               | main_function
               '''
    p[0] = ('program', p[1])


def p_main_function(p):
    '''
    main_function : TYPE_INT MAIN LEFT_PAREN RIGHT_PAREN LEFT_BRACE statement_list return_statement RIGHT_BRACE
    '''
    p[0] = ('main_function', p[1])
    print(p)


# <statement_list> ::= <statement> | <statement> <statement_list>
def p_statement_list(p):
    '''
    statement_list : statement
                   | statement statement_list
    '''
    p[0] = ('statement', p[1])


# <statement> ::= <expression_statement> | <control_statement> | <return_statement>
def p_statement(p):
    '''
    statement : expression_statement
              | control_statement
              | return_statement
    '''
    p[0] = ('statement', p[1])


# <expression_statement> ::= <expression> <semicolon>
def p_expression_statement(p):
    '''
    expression_statement : expression SEMICOLON
    '''
    p[0] = ('expression_statement', p[1])


# <control_statement> ::= <if_statement> | <while_statement> | <for_statement> | <do_while_statement>
def p_control_statement(p):
    '''
    control_statement : if_statement
                      | while_statement
                      | for_statement
                      | do_while_statement
    '''
    p[0] = ('control_statement', p[1])


# <control_keyword> ::= <while> | <if> | <else> | <do> | <for>
def p_control_keyword(p):
    '''
    control_keyword : WHILE
                    | IF
                    | ELSE
                    | DO
                    | FOR
    '''
    p[0] = ('control_keyword', p[1])


# <type_keyword> ::= <type_int>|<type_char>|<type_bool>|<type_float>
def p_type_keyword(p):
    '''
    type_keyword : TYPE_INT
                    | TYPE_FLOAT
                    | TYPE_BOOL

    '''
    p[0] = ('type_keyword', p[1])


# <if_statement> ::= <if> <left_paren> <expression> <right_paren> <left_brace> <statement> <right_brace> |
# <else if> <left_brace> <statement> <right_brace>| < else > <left_brace> <statement> <right_brace>
def p_if_statement(p):
    '''if_statement : IF LEFT_PAREN expression RIGHT_PAREN LEFT_BRACE statement RIGHT_BRACE
                    | if_statement ELSE_IF LEFT_BRACE statement RIGHT_BRACE
                    | if_statement ELSE LEFT_BRACE statement RIGHT_BRACE
    '''
    p[0] = ('if_statement', p[1])


# <while_statement> ::= <while> <left_paren> <expression> <right_paren> <left_brace> <statement> <right_brace>
def p_while_statement(p):
    '''while_statement : WHILE LEFT_PAREN expression RIGHT_PAREN LEFT_BRACE statement RIGHT_BRACE
    '''
    p[0] = ('while_statement', p[3], p[6])


# <do_while_statement> ::= <do> <left_brace> <statement> <right_brace> <while> <left_paren> <expression> <right_paren>
def p_do_while_statement(p):
    '''do_while_statement : DO LEFT_BRACE statement RIGHT_BRACE WHILE LEFT_PAREN expression RIGHT_PAREN
    '''
    p[0] = ('do_while_statement', p[3], p[7])


# <for_statement> ::= “<for> <left_paren> <assignment_expression> <semicolon> <logical_expression> <semicolon>
# <assignment_expression> <right_paren> <left_brace> <statement_list> <right_brace>
def p_for_statement(p):
    '''for_statement : FOR LEFT_PAREN assignment_expression SEMICOLON logical_expression SEMICOLON assignment_expression RIGHT_PAREN LEFT_BRACE statement_list RIGHT_BRACE
    '''
    p[0] = ('for_statement', p[3], p[6])


# <return_statement> ::= <return> <left_paren><expression><right_paren> <semicolon>
def p_return_statement(p):
    '''return_statement : RETURN number SEMICOLON
                        | RETURN SEMICOLON
    '''
    if len(p) == 3:
        p[0] = ('return_statement', p[2])
    else:
        p[0] = ('return_statement', p[3])


# <expression> ::= <assignment_expression> | <logical_expression>
def p_expression(p):
    '''expression : assignment_expression
                 | logical_expression
    '''
    p[0] = ('expression', p[1])


# <assignment_expression> ::=<type_keyword> <identifier> <assign> ( <int>|<float>| <bool>| <function_call> )
def p_assignment_expression(p):
    '''
    assignment_expression : type_keyword  IDENTIFIER ASSIGN INTEGER
                          | type_keyword  IDENTIFIER ASSIGN FLOAT
                          | type_keyword  IDENTIFIER ASSIGN TRUE
                          | type_keyword  IDENTIFIER ASSIGN FALSE
                          | type_keyword  IDENTIFIER ASSIGN function_call
    '''
    p[0] = ('assignment_expression', p[3], p[2], p[4])


# not sure about the last statement may need modification


# <logical_expression> ::= <logical_and_expression> | <logical_or_expression>  | <logical_not_expression>
def p_logical_expression(p):
    '''
    logical_expression : logical_or_expression
    '''
    p[0] = p[1]


# <logical_or_expression> ::= <logical_and_expression> (<logical_or> <logical_and_expression>)*
def p_logical_or_expression(p):
    '''
    logical_or_expression : logical_and_expression
                          | logical_and_expression LOGICAL_OR logical_and_expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('LOGICAL_OR', p[1], p[3])


# <logical_and_expression> ::= <equality_expression> (<logical_and> <equality_expression>)*
def p_logical_and_expression(p):
    '''
    logical_and_expression : equality_expression
                           | equality_expression LOGICAL_AND equality_expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('LOGICAL_AND', p[1], p[3])


# The rule above may need to be redefined


# <logical_or_expression> ::= <logical_and_expression> (<logical_or> <logical_and_expression>)*

def p_logical_not(p):
    '''logical_not_expression : LOGICAL_NOT logical_and_expression
                              | LOGICAL_NOT logical_or_expression
    '''
    p[0] = not (p[2])


def p_equality_expression(p):
    '''equality_expression : relational_expression EQUALS relational_expression
                           | relational_expression NOT_EQUALS relational_expression
    '''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]


def p_relational_expression(p):
    '''relational_expression : additive_expression LESS_THAN additive_expression
                             | additive_expression GREATER_THAN additive_expression
                             | additive_expression LESS_THAN_OR_EQUAL additive_expression
                             | additive_expression GREATER_THAN_OR_EQUAL additive_expression'''
    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>+':
        p[0] = p[1] > + p[3]


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression PLUS multiplicative_expression
                           | multiplicative_expression MINUS multiplicative_expression
                           | unary_expression MINUS unary_expression
                           | unary_expression PLUS unary_expression
    '''
    # didn't add repeating section of multiplicative , requires grammar rework
    # maybe just have two-term expressions
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_multiplicative_expression(p):
    '''multiplicative_expression    : unary_expression MULTIPLY unary_expression
                                    | unary_expression DIVIDE unary_expression'''
    # didn't add repeating section of unary , requires grammar rework
    # again, maybe just have two-term expressions
    if p[2] == '*':
        p[0] = (p[1] * p[3])
    elif p[2] == '/':
        p[0] = (p[1] / p[3])


def p_unary_expression(p):
    '''unary_expression ::= primary_expression
                            | MINUS primary_expression
                            | PLUS primary_expression
    '''
    # maybe the plus and minus should be added at the number non-terminal
    # instead of here since this can give us negative function calls
    if p[1] == '-':
        p[0] = - p[2]
    elif p[1] == '+':
        p[0] = + p[2]
    else:
        p[0] = p[1]


def p_primary_expression(p):
    '''primary_expression : IDENTIFIER
                            | number
                            | LEFT_PAREN expression RIGHT_PAREN
                            | function_call '''
    if p[1] == '(':
        p[0] = (p[1])
    else:
        p[0] = p[1]


def p_function(p):
    '''function : type_keyword IDENTIFIER LEFT_PAREN argument_list RIGHT_PAREN LEFT_BRACE statement_list RIGHT_BRACE'''
    # not really sure how commas interact here
    p[0] = p[1], p[2], (p[4]), {p[7]}


def p_function_call(p):
    '''function_call : IDENTIFIER LEFT_PAREN argument_list RIGHT_PAREN'''
    # p[0] = p[1](p[3])
    p[0] = (p[3])


def p_argument_list(p):
    '''argument_list : type_keyword expression  '''
    # not sure abt recursion, also think this should be unary expression
    p[0] = p[1], p[2]


def p_number(p):
    '''number   : INTEGER
                | FLOAT'''
    p[0] = p[1]


def p_error(p):
    print('Syntax error at {}'.format(p.value))


# create a parser instance
parser = yacc.yacc()
# parser = yacc.yacc(debug=True, write_tables=False, optimize=False, start='program', lexer=lexer)


input_str = open('input.txt', 'r')
file = input_str.read()
# call the parse method to parse the input
ast = parser.parse(file)
print(ast)
