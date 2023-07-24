// Gramàtica per lambda càlcul
grammar lc;

root : terme             // l'etiqueta ja és root
    | definir_macro
    ;

terme : terme MACRO_INF terme              # macro_infixa 
    | '(' terme ')'                        # terme_par
    | terme terme                          # aplicacio
    | LAMBDA lletres '.' terme             # abstraccio
    | LLETRA                               # lletra
    | (MACRO | MACRO_INF)                  # macro                 
    ;  

definir_macro : (MACRO | MACRO_INF) EQUIVALENCIA terme
    ;
                
LLETRA : [a-z] ;
lletres: LLETRA+ ;
LAMBDA : ('λ'|'\\') ;
EQUIVALENCIA : ('≡'|'=') ;
MACRO : [A-Z]([A-Z]|[0-9])* ;
MACRO_INF : ('/'|'*'|'-'|'+') ;
WS  : [ \t\n\r]+ -> skip ;