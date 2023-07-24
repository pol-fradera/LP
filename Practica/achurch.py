from __future__ import annotations
from antlr4 import *
from lcLexer import lcLexer
from lcParser import lcParser
from lcVisitor import lcVisitor
from dataclasses import dataclass


@dataclass
class Lletra:
    val: str


@dataclass
class Abstraccio:
    esq: Lletra
    dre: Terme


@dataclass
class Aplicacio:
    esq: Terme
    dre: Terme


Terme = Lletra | Abstraccio | Aplicacio


class TreeVisitor(lcVisitor):
    def __init__(self):
        self.macros = {}

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx):
        [terme] = list(ctx.getChildren())
        # print(len(list(terme.getChildren())))
        return self.visit(terme)

    # Visit a parse tree produced by lcParser#terme_par.
    def visitTerme_par(self, ctx):
        [_, terme, _] = list(ctx.getChildren())
        return self.visit(terme)

    # Visit a parse tree produced by lcParser#lletra.
    def visitLletra(self, ctx):
        [lletra] = list(ctx.getChildren())
        val = lletra.getText()
        return Lletra(val)

    #Crea l'arbre d'abstraccions quan hi ha més d'un paràmetre seguit
    def constructAbstraccioTree(self, lletres, terme):
        if len(lletres) == 0:
            return self.visit(terme)
        else:
            esq = Lletra(lletres[0])
            sub_arbre = self.constructAbstraccioTree(lletres[1:], terme)
            return Abstraccio(esq, sub_arbre)

    # Visit a parse tree produced by lcParser#abstraccio.
    def visitAbstraccio(self, ctx):
        [lamda, lletres, punt, terme] = list(ctx.getChildren())
        llista_lletres = self.visit(lletres)
        esq = Lletra(llista_lletres[0])
        dre = self.constructAbstraccioTree(llista_lletres[1:], terme)
        return Abstraccio(esq, dre)

    # Visit a parse tree produced by lcParser#aplicacio.
    def visitAplicacio(self, ctx):
        [terme1, terme2] = list(ctx.getChildren())
        esq = self.visit(terme1)
        dre = self.visit(terme2)
        return Aplicacio(esq, dre)

    # Visit a parse tree produced by lcParser#lletres.
    def visitLletres(self, ctx):
        lletres = list(ctx.getChildren())
        return list(map(lambda x: x.getText(), lletres))

    # Visit a parse tree produced by lcParser#definir_macro.
    def visitDefinir_macro(self, ctx):
        [macro, _, terme] = list(ctx.getChildren())
        self.macros[macro.getText()] = self.visit(terme)
        for clau in self.macros:
            valor = self.macros[clau]
            expr = imprimir_arbre(valor)
            print(clau + ' ≡ ' + expr)

    # Visit a parse tree produced by lcParser#macro.
    def visitMacro(self, ctx):
        [macro] = list(ctx.getChildren())
        return self.macros[macro.getText()]

    # Visit a parse tree produced by lcParser#macro_infixa.
    def visitMacro_infixa(self, ctx):
        [terme1, macro_inf, terme2] = list(ctx.getChildren())
        esq = self.macros[macro_inf.getText()]
        dre = self.visit(terme1)
        dre2 = self.visit(terme2)
        return Aplicacio(Aplicacio(esq, dre), dre2)


# Converteix l'arbre a string
def imprimir_arbre(a: Terme) -> str:
    match a:
        case Lletra(val):
            return val
        case Abstraccio(esq, dre):
            return '(λ' + imprimir_arbre(esq) + '.' + imprimir_arbre(dre) + ')'
        case Aplicacio(esq, dre):
            return '(' + imprimir_arbre(esq) + imprimir_arbre(dre) + ')'


# Es fa la substitució de la beta-reducció
def substitucio(valor, parametre, a: Terme) -> Terme:
    match a:
        case Lletra(val):
            if parametre.val == val:
                return valor
            else:
                return a
        case Abstraccio(esq, dre):
            nou_dre = substitucio(valor, parametre, dre)
            return Abstraccio(esq, nou_dre)
        case Aplicacio(esq, dre):
            nou_esq = substitucio(valor, parametre, esq)
            nou_dre = substitucio(valor, parametre, dre)
            return Aplicacio(nou_esq, nou_dre)


# Es realitza l'alfa conversió, les variables var es substituexien per una variable fresca
def realitzar_alfa_conversio(a: Terme, var, var_fresca) -> Terme:
    match a:
        case Abstraccio(esq, dre):
            if esq.val == var:
                esq = Lletra(var_fresca)
            nou_dre = realitzar_alfa_conversio(dre, var, var_fresca)
            return Abstraccio(esq, nou_dre)
        case Aplicacio(esq, dre):
            nou_esq = realitzar_alfa_conversio(esq, var, var_fresca)
            nou_dre = realitzar_alfa_conversio(dre, var, var_fresca)
            return Aplicacio(nou_esq, nou_dre)
        case Lletra(varl):
            if varl == var:
                varl = var_fresca
            return Lletra(varl)

# A set_var hi haurà el conjunt de variables usades al terme a
# tant com a paràmetre com a retorn
def obternir_var_usades(a: Terme, set_var):
    match a:
        case Abstraccio(esq, dre):
            set_var.add(esq.val)
            obternir_var_usades(dre, set_var)
        case Aplicacio(esq, dre):
            obternir_var_usades(esq, set_var)
            obternir_var_usades(dre, set_var)
        case Lletra(val):
            set_var.add(val)


# A set_var hi haurà el conjunt de variables usades al terme a
def obtenir_variables(a: Terme, set_var):
    match a:
        case Abstraccio(esq, dre):
            obtenir_variables(dre, set_var)
        case Aplicacio(esq, dre):
            obtenir_variables(esq, set_var)
            obtenir_variables(dre, set_var)
        case Lletra(val):
            set_var.add(val)

# A set_param hi haurà el conjunt de variables usades com a paràmetre al terme a
def obtenir_parametres(a: Terme, set_param):
    match a:
        case Abstraccio(esq, dre):
            set_param.add(esq.val)
            obtenir_parametres(dre, set_param)
        case Aplicacio(esq, dre):
            obtenir_parametres(esq, set_param)
            obtenir_parametres(dre, set_param)

# Es retorna el terme a reduït i un booleà indicant si s'ha pogut aplicar una beta-reducció
def aplicar_beta_reduccio(a: Terme) -> (Terme, bool):
    match a:
        case Aplicacio(esq, dre):
            match esq:
                case Abstraccio(_, _):
                    set_param_esq = set()
                    set_param_dre = set()
                    set_var_dre = set()
                    obtenir_parametres(esq, set_param_esq)
                    obtenir_parametres(dre, set_param_dre)
                    obtenir_variables(dre, set_var_dre)
                    variables_comunes = set_param_esq.intersection(set_var_dre.difference(set_param_dre))
                    set_var_usades = set()
                    obternir_var_usades(esq, set_var_usades)
                    terme_convertit = esq
                    for variable in variables_comunes:
                        # Obtenir la primera lletra no usada
                        for x in range(ord('a'), ord('z')+1):
                            lletra = chr(x)
                            if lletra not in set_var_usades:
                                nova_variable = lletra
                                set_var_usades.add(nova_variable)
                                break
                        terme_convertit_ant = terme_convertit
                        terme_convertit = realitzar_alfa_conversio(terme_convertit, variable, nova_variable)
                        print('α-conversió: ' + variable + ' → ' + nova_variable)
                        print(imprimir_arbre(terme_convertit_ant) + ' → ' + imprimir_arbre(terme_convertit))

                    nou_terme = substitucio(dre, terme_convertit.esq, terme_convertit.dre)
                    arbre_convertit = Aplicacio(terme_convertit, dre)
                    print('β-reducció:')
                    print(imprimir_arbre(arbre_convertit) + ' → ' + imprimir_arbre(nou_terme))
                    return nou_terme, True
                case _:
                    nou_esq, reduccio_esq = aplicar_beta_reduccio(esq)
                    nou_dre, reduccio_dre = aplicar_beta_reduccio(dre)
                    return Aplicacio(nou_esq, nou_dre), reduccio_esq or reduccio_dre
        case Abstraccio(esq, dre):
            nou_dre, reduccio_dre = aplicar_beta_reduccio(dre)
            return Abstraccio(esq, nou_dre), reduccio_dre
        case _:
            return a, False

# Es retorna el terme reduït i un booleà indicant si s'ha pogut fer sobre el límit d'iteraccions
def realitzar_beta_reduccions(a: Terme) -> (Terme, bool):
    n = 1
    reduccio_realitzada = True
    while reduccio_realitzada:
        b = a
        a, reduccio_realitzada = aplicar_beta_reduccio(b)
        if reduccio_realitzada:
            n += 1
        if n >= 40:
            return a, False
    return a, True


def main():
    visitor = TreeVisitor()

    while True:
        input_stream = InputStream(input('? '))
        # input_stream = FileStream("input.txt")
        lexer = lcLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = lcParser(token_stream)
        tree = parser.root()

        if parser.getNumberOfSyntaxErrors() == 0:
            arbre = visitor.visit(tree)
            match arbre:
                case Lletra(_) | Abstraccio(_, _) | Aplicacio(_, _):
                    exp = imprimir_arbre(arbre)
                    print('Arbre:')
                    print(exp)
                    arbre_reduit, correcte = realitzar_beta_reduccions(arbre)
                    exp2 = imprimir_arbre(arbre_reduit)
                    print('Resultat:')
                    if correcte:
                        print(exp2)
                    else:
                        print("Nothing")
        else:
            print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
            print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main()
