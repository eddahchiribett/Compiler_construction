grammar AN_RULES;

program : function main_function
        | main_function
        ;
        
main_function   : TYPE_INT MAIN LPAREN RPAREN LBRACE statement_list RETURN SEMICOLON RBRACE ;

statement_list  : statement 
                | statement statement_list
                ;
statement   : expression_statement 
            | control_statement 
            | return_statement
            | print_statement
            ;
            
expression_statement : expression SEMICOLON ;

control_statement   : if_statement 
                    | while_statement 
                    | for_statement 
                    | do_while_statement;
control_keyword : WHILE | IF | ELSE | DO | FOR ;
type_keyword    : TYPE_INT
                |TYPE_BOOL
                |TYPE_FLOAT
                ;
if_statement    : IF LPAREN expression RPAREN LBRACE statement RBRACE 
                | IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE  LBRACE statement RBRACE
                | IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE IF LBRACE statement RBRACE  ELSE  LBRACE statement RBRACE
                ;
while_statement : WHILE LPAREN expression RPAREN LBRACE statement RBRACE;

do_while_statement : DO LBRACE statement RBRACE WHILE LPAREN expression RPAREN;

for_statement : FOR LPAREN assignment_expression logical_expression assignment_expression RPAREN  LBRACE statement_list RBRACE;

return_statement : RETURN LPAREN expression RPAREN SEMICOLON;
print_statement : PRINT LPAREN STRING RPAREN SEMICOLON ;

expression  : assignment_expression 
            | logical_expression
            | unary_expression
            ;
            
assignment_expression   :type_keyword IDENTIFIER ASSIGN INT
                        |type_keyword IDENTIFIER ASSIGN FLOAT
                        |type_keyword IDENTIFIER ASSIGN TRUE
                        |type_keyword IDENTIFIER ASSIGN FALSE
                        |type_keyword IDENTIFIER ASSIGN expression MULTIPLY expression
                        |type_keyword IDENTIFIER ASSIGN expression DIVIDE expression
                        |type_keyword IDENTIFIER ASSIGN expression PLUS expression
                        |type_keyword IDENTIFIER ASSIGN expression MINUS expression
                        |type_keyword IDENTIFIER ASSIGN function_call 
                        ;
logical_expression      : logical_or_expression
                        | logical_not_expression;

logical_or_expression : logical_and_expression (LOGICAL_OR logical_and_expression)*;

logical_and_expression: equality_expression (LOGICAL_AND equality_expression)*;

logical_not_expression  : LOGICAL_NOT logical_and_expression 
                        | LOGICAL_NOT logical_or_expression 
                        ;
equality_expression : relational_expression EQUALS relational_expression 
                    | relational_expression NOT_EQUALS relational_expression
                    ;
relational_expression   : additive_expression LESS_THAN additive_expression
                        | additive_expression GREATER_THAN additive_expression
                        | additive_expression LESS_THAN_OR_EQUAL additive_expression
                        | additive_expression GREATER_THAN_OR_EQUAL additive_expression
                        ;
additive_expression     : multiplicative_expression PLUS multiplicative_expression 
                        | multiplicative_expression MINUS multiplicative_expression
                        ;
                        
multiplicative_expression   : unary_expression MULTIPLY unary_expression
                            | unary_expression DIVIDE unary_expression
                            ;
unary_expression    : primary_expression 
                    | MINUS primary_expression 
                    | PLUS primary_expression
                    ;
primary_expression  : IDENTIFIER 
                    | number 
                    | LPAREN expression RPAREN 
                    | function_call
                    ;
function : type_keyword IDENTIFIER LPAREN argument_list RPAREN LBRACE statement_list RBRACE;
function_call : IDENTIFIER LPAREN argument_list RPAREN;
argument_list : type_keyword expression (COMMA type_keyword expression)*;
number  : INT
        | FLOAT;
        

LOGICAL_AND : '&&' ;
LOGICAL_OR : '||' ;
LOGICAL_NOT : '!' ;
ASSIGN : '=' ;
COMMA : ',' ;
SEMICOLON : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
L_BRACKET : '[' ;
R_BRACKET : ']' ;
EQUALS : '==';
TYPE_INT: 'int';
TYPE_FLOAT: 'float';
TYPE_BOOL: 'bool';
TYPE_STRING:  'string';
WHILE : 'while';

ELSE :'else';
DO:'do';
FOR:'for';
IF : 'if';
PRINT :'print';
INPUT :'input';
ELSE_IF:'else if';
TRUE:'true';
FALSE:'false';
VOID: 'void';
MAIN:'main';
RETURN :'return';


MINUS :'-';
PLUS: '+';
MULTIPLY: '*';
DIVIDE :'/';
BACKSLASH: '\\';
MODULUS: '%';
NOT_EQUALS:'!=';
LESS_THAN:'<';
GREATER_THAN:'>';
LESS_THAN_OR_EQUAL:'<=';
GREATER_THAN_OR_EQUAL:'>=';


INT : [-+]? [0-9]+ ;
FLOAT: [-+]? [0-9]+.[0-9]+;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING :  '"' ('\\' ["\\] | ~["\\\r\n])* '"';
WS: [ \t\n\r\f]+ -> skip ;












