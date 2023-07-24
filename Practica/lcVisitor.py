# Generated from lc.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .lcParser import lcParser
else:
    from lcParser import lcParser

# This class defines a complete generic visitor for a parse tree produced by lcParser.

class lcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lcParser#root.
    def visitRoot(self, ctx:lcParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#terme_par.
    def visitTerme_par(self, ctx:lcParser.Terme_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#macro.
    def visitMacro(self, ctx:lcParser.MacroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#lletra.
    def visitLletra(self, ctx:lcParser.LletraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#abstraccio.
    def visitAbstraccio(self, ctx:lcParser.AbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#macro_infixa.
    def visitMacro_infixa(self, ctx:lcParser.Macro_infixaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#aplicacio.
    def visitAplicacio(self, ctx:lcParser.AplicacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#definir_macro.
    def visitDefinir_macro(self, ctx:lcParser.Definir_macroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lcParser#lletres.
    def visitLletres(self, ctx:lcParser.LletresContext):
        return self.visitChildren(ctx)



del lcParser