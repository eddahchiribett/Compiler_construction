import logging
import ply.yacc as yacc
import lexer

logging.getLogger('ply').setLevel(logging.WARNING)

tokens = lexer.tokens
token_string = lexer.token_string
print('\nOutput string from the lexer is: \n')
print(token_string)
print('\n')

temp_count = 1
label_count = 1
intermediate_code = []
intermediate_code.append("PROGRAM START:")


# generate a temporary variable
def new_temp():
    global temp_count
    new_temp = "t" + str(temp_count)
    temp_count += 1
    return new_temp


# generate a label
def new_label():
    global label_count
    new_label = "L" + str(label_count)
    label_count += 1
    return new_label


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
)


# Define the grammar rules
def p_program(p):
    '''
    program : function main_function
            | main_function
    '''
    if len(p) == 3:
        p[0] = ['program', p[1], p[2]]
    elif len(p) == 2:
        p[0] = ['program', p[1]]


def p_main_function(p):
    '''
    main_function : TYPE_INT MAIN LPAREN RPAREN LBRACE statement_list RBRACE
    '''
    p[0] = ('main_function', p[6])


def p_statement_list(p):
    '''
    statement_list : statement
                   | statement statement_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


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
                 | IF LPAREN expression RPAREN LBRACE statement RBRACE ELIF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement RBRACE
    '''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
        # t1 = p[3]
        # t2 = !t1
        # if (t2) goto L1
        # p[6]
        # L1:
        t1 = new_temp()
        t2 = new_temp()
        # intermediate_code.append(t1 + ' = ' + str(p[3][1]))
        # intermediate_code.append(t2 + ' = ' + '!t1')
        # intermediate_code.append('if ' + t2 + ' goto ' + new_label())
        # intermediate_code.append(p[6][1])
        # intermediate_code.append(new_label() + ':')
        intermediate_code.append(t1 + ' = ' + str(p[3]))
        intermediate_code.append(t2 + ' = ' + '!' + t1)
        intermediate_code.append('if ' + t2 + ' goto ' + new_label())
        intermediate_code.append(p[6][1])
        intermediate_code.append(new_label() + ':')
    elif len(p) == 12:
        p[0] = (('if', p[3], p[6]), ('else', p[10]))
        # t1 = p[3]
        # t2 = !t1
        # if (t2) goto L1
        # p[6]
        # goto L2
        # L1:
        # p[10]
        # L2:
        t1 = new_temp()
        t2 = new_temp()
        L1 = new_label()
        L2 = new_label()
        intermediate_code.append(t1 + ' = ' + str(p[3][1]))
        intermediate_code.append(t2 + ' = ' + '!' + t1)
        intermediate_code.append('if ' + t2 + ' goto ' + L1)
        intermediate_code.append(p[6])
        intermediate_code.append('goto ' + L2)
        intermediate_code.append(L1 + ':')
        intermediate_code.append(p[10])
        intermediate_code.append(L2 + ':')
    elif len(p) == 19:
        p[0] = (('if', p[3], p[6]), ('elif', p[10], p[13]), ('else', p[17]))

        # t1 = p[3]//conditional for if
        # t2 = !t1
        # t3 = p[10] //conditional for elif
        # t4 = !t3
        # if (t2) goto L1
        # p[6]
        # goto L3
        # L1:
        # if (t4) goto L2:
        # p[13]
        # goto L3
        # L2:
        # p[17]
        # goto L3
        # L3: //exit

        t1 = new_temp()
        t2 = new_temp()
        t3 = new_temp()
        t4 = new_temp()
        L1 = new_label()
        L2 = new_label()
        L3 = new_label()
        intermediate_code.append(t1 + ' = ' + str(p[3][1]))
        intermediate_code.append(t2 + ' = ' + '!' + t1)
        intermediate_code.append(t3 + ' = ' + str(p[10][1]))
        intermediate_code.append(t4 + ' = ' + '!' + t3)
        intermediate_code.append('if ' + t2 + ' goto ' + L2)
        intermediate_code.append(p[6])
        intermediate_code.append('goto ' + L3)
        intermediate_code.append(L1 + ':')
        intermediate_code.append('if ' + t4 + ' goto ' + L2)
        intermediate_code.append(p[13])
        intermediate_code.append('goto ' + L3)
        intermediate_code.append(L2 + ':')
        intermediate_code.append(p[17])
        intermediate_code.append('goto ' + L3)
        intermediate_code.append(L3 + ':')


def p_while_statement(p):
    '''
    while_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE
    '''
    p[0] = ('while_statement', p[3], p[6])
    t1 = new_temp()
    t2 = new_temp()
    L1 = new_label()  # Start of the loop
    L2 = new_label()  # End of the loop
    intermediate_code.append(L1 + ':')
    intermediate_code.append(t1 + ' = ' + str(p[3][1]))  # Evaluate the condition
    intermediate_code.append(t2 + ' = ' + '!' + t1)  # Negate the condition
    intermediate_code.append('if ' + t2 + ' goto ' + L2)  # If condition is false, jump to the end of the loop
    intermediate_code.append(p[6])  # Execute the loop body
    intermediate_code.append('goto ' + L1)  # Jump back to the start of the loop
    intermediate_code.append(L2 + ':')  # End of the loop


def p_do_while_statement(p):
    '''
    do_while_statement : DO LBRACE statement RBRACE WHILE LPAREN expression RPAREN SEMICOLON
    '''
    p[0] = ('do_while_statement', p[7], p[3])
    t1 = new_temp()
    L1 = new_label()
    L2 = new_label()

    intermediate_code.append(L1 + ':')
    intermediate_code.append(p[3])
    intermediate_code.append(t1 + ' = ' + str(p[7][1]))
    intermediate_code.append('if ' + t1 + ' goto ' + L1)
    intermediate_code.append(L2 + ':')


def p_return_statement(p):
    '''return_statement : RETURN LPAREN INTEGER RPAREN SEMICOLON
                        | RETURN LPAREN FLOAT RPAREN SEMICOLON
                        | RETURN LPAREN TRUE RPAREN SEMICOLON
                        | RETURN LPAREN FALSE RPAREN SEMICOLON
    '''
    p[0] = ('return_statement', p[3])
    t1 = new_temp()
    intermediate_code.append(t1 + ' = ' + str(p[0]))


def p_print_statement(p):
    '''
    print_statement : PRINT LPAREN STRING RPAREN SEMICOLON
    '''
    p[0] = ('print', p[3])
    t1 = new_temp()
    intermediate_code.append(t1 + ' = ' + str(p[0]))


def p_expression(p):
    '''
    expression  : assignment_expression
                | logical_expression
                | unary_expression
                | arithmetic_expression
                | relational_expression
                | equality_expression
                | TRUE
                | FALSE
    '''
    p[0] = ('exp', p[1])
    return p[1]


def p_arithmetic_expression(p):
    '''
    arithmetic_expression   : IDENTIFIER PLUS IDENTIFIER
                            | IDENTIFIER PLUS INTEGER
                            | IDENTIFIER MODULUS IDENTIFIER
                            | IDENTIFIER MINUS IDENTIFIER
                            | IDENTIFIER MINUS INTEGER
                            | IDENTIFIER MINUS FLOAT
                            | IDENTIFIER MODULUS INTEGER
                            | IDENTIFIER MULTIPLY IDENTIFIER
                            | IDENTIFIER MULTIPLY INTEGER
                            | IDENTIFIER MULTIPLY FLOAT
                            | IDENTIFIER DIVIDE IDENTIFIER
                            | IDENTIFIER DIVIDE INTEGER
                            | IDENTIFIER DIVIDE FLOAT
                            | INTEGER PLUS INTEGER
                            | INTEGER MULTIPLY INTEGER
                            | INTEGER MINUS INTEGER
                            | INTEGER PLUS IDENTIFIER
                            | INTEGER DIVIDE INTEGER
                            | INTEGER MODULUS IDENTIFIER
                            | INTEGER MODULUS INTEGER
                            | FLOAT PLUS FLOAT
                            | FLOAT MINUS FLOAT
                            | FLOAT MULTIPLY FLOAT
                            | FLOAT DIVIDE FLOAT
    '''
    p[0] = ('arithmetic_exp', p[2], p[1], p[3])
    t1 = new_temp()
    if type(p[1]) == float and type(p[3]) == float:
        intermediate_code.append(t1 + ' = ' + str(p[1]) + p[2] + str(p[3]))

    else:
        intermediate_code.append(t1 + ' = ' + str(p[1]) + str(p[2]) + str(p[3]))


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
    if len(p) == 5:
        p[0] = ('assignment_exp', p[3], p[2], p[4])
        intermediate_code.append(p[2] + ' = ' + str(p[4]))
    elif len(p) == 4:
        p[0] = ('assignment_exp', p[2], p[1], p[3])
        intermediate_code.append(p[1] + ' = ' + str(p[3]))


def p_logical_expression(p):
    '''
    logical_expression : logical_or_expression
                       | logical_and_expression
                       | logical_not_expression
    '''
    p[0] = ('logical_exp', p[1])


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
    p[0] = ('logical_or', p[2], p[1], p[3])
    intermediate_code.append(p[1][1] + ' OR ' + p[3][1])


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
    # t1 = new_temp()
    p[0] = ('logical_and', p[1], p[2], p[3])
    # intermediate_code.append(t1 + '= ' + str(p[1]) + ' AND ' +str(p[3]))


def p_logical_not_expression(p):
    '''logical_not_expression   : LOGICAL_NOT logical_and_expression
                                | LOGICAL_NOT logical_or_expression
                                | LOGICAL_NOT IDENTIFIER
                                | LOGICAL_NOT equality_expression
                                | LOGICAL_NOT relational_expression
    '''
    p[0] = ('logical_not', p[1], p[2])
    # t11 = new_temp()
    # intermediate_code.append('t11 ' + '= ' + 'NOT ' + p[1][1])


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
    p[0] = ('equality_exp', p[2], p[1], p[3])
    t1 = new_temp()
    if p[2] == '==':
        intermediate_code.append(t1 + '= ' + p[1] + p[2] + p[3])
    else:
        intermediate_code.append(t1 + '= ' + p[1] + p[2] + p[3])


def p_relational_expression(p):
    ''' relational_expression   : IDENTIFIER GREATER_THAN IDENTIFIER
                                | IDENTIFIER GREATER_THAN INTEGER
                                | IDENTIFIER GREATER_THAN FLOAT
                                | IDENTIFIER LESS_THAN IDENTIFIER
                                | IDENTIFIER LESS_THAN INTEGER
                                | IDENTIFIER LESS_THAN FLOAT
                                | IDENTIFIER LESS_THAN_OR_EQUAL IDENTIFIER
                                | IDENTIFIER LESS_THAN_OR_EQUAL INTEGER
                                | IDENTIFIER LESS_THAN_OR_EQUAL FLOAT
                                | IDENTIFIER GREATER_THAN_OR_EQUAL IDENTIFIER
                                | IDENTIFIER GREATER_THAN_OR_EQUAL INTEGER
                                | IDENTIFIER GREATER_THAN_OR_EQUAL FLOAT
                                | INTEGER GREATER_THAN IDENTIFIER
                                | INTEGER GREATER_THAN INTEGER
                                | INTEGER GREATER_THAN FLOAT
                                | INTEGER LESS_THAN IDENTIFIER
                                | INTEGER LESS_THAN INTEGER
                                | INTEGER LESS_THAN FLOAT
                                | INTEGER LESS_THAN_OR_EQUAL IDENTIFIER
                                | INTEGER LESS_THAN_OR_EQUAL INTEGER
                                | INTEGER LESS_THAN_OR_EQUAL FLOAT
                                | INTEGER GREATER_THAN_OR_EQUAL IDENTIFIER
                                | INTEGER GREATER_THAN_OR_EQUAL INTEGER
                                | INTEGER GREATER_THAN_OR_EQUAL FLOAT
                                | FLOAT GREATER_THAN IDENTIFIER
                                | FLOAT GREATER_THAN INTEGER
                                | FLOAT GREATER_THAN FLOAT
                                | FLOAT LESS_THAN IDENTIFIER
                                | FLOAT LESS_THAN INTEGER
                                | FLOAT LESS_THAN FLOAT
                                | FLOAT LESS_THAN_OR_EQUAL IDENTIFIER
                                | FLOAT LESS_THAN_OR_EQUAL INTEGER
                                | FLOAT LESS_THAN_OR_EQUAL FLOAT
                                | FLOAT GREATER_THAN_OR_EQUAL IDENTIFIER
                                | FLOAT GREATER_THAN_OR_EQUAL INTEGER
                                | FLOAT GREATER_THAN_OR_EQUAL FLOAT
    '''
    p[0] = (p[1], p[2], p[3])


def p_unary_expression(p):
    '''unary_expression   : MINUS number
                          | PLUS number
                          | function_call
                          | IDENTIFIER
                          | LPAREN expression RPAREN
    '''
    if len(p) == 4:
        p[0] = ('unary_exp', p[1], p[2], p[3])
        intermediate_code.append(p[1] + p[2])
    elif len(p) == 3:
        p[0] = ('unary_exp', p[1], p[2])
        intermediate_code.append(p[1] + p[2])
    else:
        p[0] = ('unary_exp', p[1])


def p_function(p):
    '''
    function : type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE
             | VOID IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE
    '''
    p[0] = ('function', p[1], p[2], p[4], p[7])
    intermediate_code.insert(1, f"{p[2]} FUNCTION START:")


def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN argument_list RPAREN
    '''
    p[0] = ('function_call', p[1], p[3])


def p_argument_list(p):
    '''
    argument_list : argument
                  | argument COMMA argument_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_argument(p):
    '''
    argument : type_keyword IDENTIFIER
             | IDENTIFIER
    '''
    if len(p) == 3:
        p[0] = ('argument', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('argument', p[1])


def p_number(p):
    '''number : INTEGER
              | FLOAT
    '''
    p[0] = ('number', p[1])


def p_error(p):
    print('Syntax error at {}'.format(p.value))


# create a parser instance
parser = yacc.yacc()
# parser = yacc.yacc(debug=True, write_tables=False, optimize=False, start='program', lexer=lexer)


# call the parse method to parse the token string
ast = parser.parse(token_string)
print('The parse tree for the input token string is: \n')
print(ast)
print('\n')
# print the intermediate code
for line in intermediate_code:
    print(line)
