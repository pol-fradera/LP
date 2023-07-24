# Generated from exprs.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#lines.
    def visitLines(self, ctx:exprsParser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#define_var.
    def visitDefine_var(self, ctx:exprsParser.Define_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#write.
    def visitWrite(self, ctx:exprsParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#if.
    def visitIf(self, ctx:exprsParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#while.
    def visitWhile(self, ctx:exprsParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#crida_funcio.
    def visitCrida_funcio(self, ctx:exprsParser.Crida_funcioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#potencia.
    def visitPotencia(self, ctx:exprsParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#multiplicacio_divisio.
    def visitMultiplicacio_divisio(self, ctx:exprsParser.Multiplicacio_divisioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#suma_resta.
    def visitSuma_resta(self, ctx:exprsParser.Suma_restaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#boolea.
    def visitBoolea(self, ctx:exprsParser.BooleaContext):
        return self.visitChildren(ctx)



del exprsParser