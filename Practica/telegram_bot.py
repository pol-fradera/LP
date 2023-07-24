from __future__ import annotations
from achurch import *
import pydot
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from dataclasses import dataclass

# Variables globals
visitor = TreeVisitor()
reduccions = ''

# Es retorna el terme a reduït i un booleà indicant si s'ha pogut aplicar una beta-reducció
def aplicar_beta_reduccio(a: Terme) -> (Terme, bool):
    global reduccions
    match a:
        case Aplicacio(esq, dre):
            match esq:
                case Abstraccio(esq2, dre2):
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
                        reduccions += imprimir_arbre(terme_convertit_ant) + ' →α→ ' + imprimir_arbre(terme_convertit) + '\n'

                    nou_terme = substitucio(dre, terme_convertit.esq, terme_convertit.dre)
                    arbre_convertit = Aplicacio(terme_convertit, dre)
                    reduccions += imprimir_arbre(arbre_convertit) + ' →β→ ' + imprimir_arbre(nou_terme) + '\n'
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


# Definició de la comanda start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'AChurchBot!\nBenvingut {update.effective_user.first_name}!')


# Definició de la comanda author
async def author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="AChurchBot!\n@ Pol Fradera Insa, 2023")


# Definició de la comanda help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/start\n/author\n/help\n/macros\nExpressió λ-càlcul")


# Definició de la comanda macors
async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resp = ''
    if len(visitor.macros) == 0:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='No s\'ha definit cap macro.')
    else:
        for clau in visitor.macros:
            valor = visitor.macros[clau]
            expr = imprimir_arbre(valor)
            resp += clau + ' ≡ ' + expr + '\n'
        if resp != '':
            await context.bot.send_message(chat_id=update.effective_chat.id, text=resp)


# A graph hi haurà l'arbre a com a objecte pydot.Dot
# parametres és un diccionari amb tots els paràmtres de les abstraccions 
# (la clau és la variable i el valor el nom del node), s'utilitza per les arestes de les variables lligades
# father és el node pare de a 
def construir_graf(a: Terme, graph, father, parametres):
    nodes = graph.get_nodes()
    node_count = len(nodes)
    match a:
        case Aplicacio(esq, dre):
            graph.add_node(pydot.Node(node_count, label="@", shape="none"))
            if father >= 0:
                graph.add_edge(pydot.Edge(father, node_count))
            parametres_copy = parametres.copy()
            construir_graf(esq, graph, node_count, parametres)
            construir_graf(dre, graph, node_count, parametres_copy)
        case Abstraccio(esq, dre):
            graph.add_node(pydot.Node(node_count, label="λ" + esq.val, shape="none"))
            if father >= 0:
                graph.add_edge(pydot.Edge(father, node_count))

            parametres[esq.val] = node_count
            construir_graf(dre, graph, node_count, parametres)
        case Lletra(val):
            graph.add_node(pydot.Node(node_count, label=val, shape="none"))
            if father >= 0:
                graph.add_edge(pydot.Edge(father, node_count))
                if val in parametres:
                    graph.add_edge(pydot.Edge(node_count, parametres[val], style="dotted"))

# Definició del mètode resposta del bot
async def resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global reduccions
    reduccions = ''
    input_stream = InputStream(update.message.text)
    lexer = lcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lcParser(token_stream)
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() == 0:
        arbre = visitor.visit(tree)
        match arbre:
            case Lletra(_) | Abstraccio(_, _) | Aplicacio(_, _):
                exp = imprimir_arbre(arbre)
                await context.bot.send_message(chat_id=update.effective_chat.id, text=exp)

                graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white")
                construir_graf(arbre, graph, -1, {})
                output_graph = graph.create_png()
                await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=output_graph)

                arbre_reduit, correcte = realitzar_beta_reduccions(arbre)
                resp = reduccions
                resp_list = list(resp.split('\n'))
                for x in resp_list:
                    if x != '':
                        await context.bot.send_message(chat_id=update.effective_chat.id, text=x)

                exp2 = imprimir_arbre(arbre_reduit)
                if correcte:
                    if exp != exp2:
                        await context.bot.send_message(chat_id=update.effective_chat.id, text=exp2)

                        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white")
                        construir_graf(arbre_reduit, graph, -1, {})
                        output_graph = graph.create_png()
                        await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=output_graph)
                else:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text='The maximum limit of β-reductions has been reached.')
    else:
        resp = str(parser.getNumberOfSyntaxErrors())
        if parser.getNumberOfSyntaxErrors() == 1:
            resp += ' error de sintaxi.\n'
        else:
            resp += ' errors de sintaxi.\n'
        resp += tree.toStringTree(recog=parser)

        resp_list = list(resp.split('\n'))
        for x in resp_list:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=x)


def main():
    app = ApplicationBuilder().token('6154602031:AAEN8tptXa84n7Nyn1nmzfasrAsVCfzz754').build()

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    author_handler = CommandHandler('author', author)
    app.add_handler(author_handler)

    help_handler = CommandHandler('help', help)
    app.add_handler(help_handler)

    macros_handler = CommandHandler('macros', macros)
    app.add_handler(macros_handler)

    resposta_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), resposta)
    app.add_handler(resposta_handler)

    app.run_polling()


if __name__ == "__main__":
    main()
