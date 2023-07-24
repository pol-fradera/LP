// Gramàtica per expressions senzilles
grammar exprs;
root : lines             // l'etiqueta ja és root
    ;

lines : line+
    ;

line : VAR ':=' expr                   # define_var
    | 'write' expr                     # write
    | 'if' expr 'then' lines 'end'     # if
    | 'while' expr 'do' lines 'end'    # while
    ;

expr : <assoc=right> expr '^' expr      # potencia
    | expr ('*'|'/') expr              # multiplicacio_divisio  
    | expr ('+'|'-') expr              # suma_resta 
    | expr CMP expr                    # boolea
    | NUM                              # numero
    | VAR                              # variable
    | NOM '(' VARS ')'                 # crida_funcio
    ;

NUM : [0-9]+ ;
VAR : [a-z] ;
VARS: [a-z]+  VARS2* ;
VARS2 : ',' [a-z]+ ;
NOM : [a-z]+ ;
CMP : ('='|'<'|'>'|'<>'|'<='|'>=') ;
WS  : [ \t\n\r]+ -> skip ;