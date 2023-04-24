import ply.lex as lex

# List of token names
tokens = [
    'IDENTIFIER',
    'INTEGER',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULUS',
    'ASSIGN',
    'EQUALS',
    'NOT_EQUALS',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_OR_EQUAL',
    'GREATER_THAN_OR_EQUAL',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'LOGICAL_NOT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'TYPE_INT',
    'TYPE_FLOAT',
    'TYPE_BOOL',
    'WHILE',
    'ELSE',
    'DO',
    'IF',
    'PRINT',
    'ELIF',
    'TRUE',
    'FALSE',
    'VOID',
    'MAIN',
    'RETURN',
]

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULUS = r'%'
t_ASSIGN = r'='
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_OR_EQUAL = r'<='
t_GREATER_THAN_OR_EQUAL = r'>='
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_SEMICOLON = r';'


# Regular expression rules with action code
# Float comes before integer function
def t_FLOAT(t):
    r'[-+]?\d+\.\d+'
    t.value = float(t.value)
    t.type = 'FLOAT'
    return t


def t_INTEGER(t):
    r'[-+]?(([1-9][0-9]*)|0)'
    t.type = 'INTEGER'
    return t


def t_STRING(t):
    r'\"[^\"\n]*\"'
    t.type = 'STRING'
    return t


# keywords and identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value == 'int':
        t.type = 'TYPE_INT'
    elif t.value == 'float':
        t.type = 'TYPE_FLOAT'
    elif t.value == 'bool':
        t.type = 'TYPE_BOOL'
    elif t.value == 'true':
        t.type = 'TRUE'
    elif t.value == 'false':
        t.type = 'FALSE'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'do':
        t.type = 'DO'
    elif t.value == 'for':
        t.type = 'FOR'
    elif t.value == 'print':
        t.type = 'PRINT'
    elif t.value == 'if':
        t.type = 'IF'
    elif t.value == 'elif':
        t.type = 'ELIF'
    elif t.value == 'else':
        t.type = 'ELSE'
    elif t.value == 'void':
        t.type = 'VOID'
    elif t.value == 'main':
        t.type = 'MAIN'
    elif t.value == 'return':
        t.type = 'RETURN'
    else:
        t.type = 'IDENTIFIER'
    return t


# Ignored characters (whitespace)
t_ignore = ' \t\n\r\v'


# Define a regular expression for a newline character
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    # print("Illegal character found '%s'" % t.value[0])
    print("Illegal character found '{} ' ".format(t.value[0]))
    t.lexer.skip(1)


# Create the lexer
lexer = lex.lex()

# Open the input text file
with open('input.txt', 'r') as file:
    input_text = file.read()
    print(input_text)

# Pass the input text to the lexer
lexer.input(input_text)


# Iterate over the lexer tokens and print them
token_list = []

# read the lexemes and append them to a list
for tok in lexer:
    # token_list.append(' {}, {} '.format(tok.type, tok.value))
    print('Token: {} Value: {}'.format(tok.type, tok.value))
    token_list.append('{} '.format(tok.value))


# convert the list of lexemes into a string of lexemes that match the tokens in the grammar
token_string = ' '.join(token_list)
# print(token_string)
# print('\n')

