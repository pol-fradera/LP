from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0
    def visitSuma_resta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + operador.getText())
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
    def visitMultiplicacio_divisio(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + operador.getText())
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
    def visitPotencia(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + operador.getText())
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())


class EvalVisitor(exprsVisitor):
    def __init__(self):
        self.variables = {}

    def visitRoot(self, ctx):
        [lines] = list(ctx.getChildren())
        self.visit(lines)

    def visitLines(self, ctx):
        lines = list(ctx.getChildren())
        for x in lines:
            self.visit(x)

    def visitDefine_var(self, ctx):
        [variable, _, expressio] = list(ctx.getChildren())
        self.variables[variable.getText()] = self.visit(expressio)

    def visitWrite(self, ctx):
        [_, expressio] = list(ctx.getChildren())
        print(self.visit(expressio))

    def visitIf(self, ctx):
        [_, boolea, _, lines, _] = list(ctx.getChildren())
        if self.visit(boolea):
            self.visit(lines)

    def visitWhile(self, ctx):
        [_, boolea, _, lines, _] = list(ctx.getChildren())
        while self.visit(boolea):
            self.visit(lines)

    def visitSuma_resta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == '+':
            return self.visit(expressio1) + self.visit(expressio2)
        return self.visit(expressio1) - self.visit(expressio2)

    def visitMultiplicacio_divisio(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == '*':
            return self.visit(expressio1) * self.visit(expressio2)
        return self.visit(expressio1) / self.visit(expressio2)

    def visitPotencia(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) ** self.visit(expressio2)

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())

    def visitVariable(self, ctx):
        [variable] = list(ctx.getChildren())
        return int(self.variables[variable.getText()])
    
    def visitBoolea(self, ctx):
        [expressio1, comperador, expressio2] = list(ctx.getChildren())
        if comperador.getText() == '=':
            return self.visit(expressio1) == self.visit(expressio2)
        elif comperador.getText() == '<':
            return self.visit(expressio1) < self.visit(expressio2)
        elif comperador.getText() == '>':
            return self.visit(expressio1) > self.visit(expressio2)
        elif comperador.getText() == '<>':
            return self.visit(expressio1) != self.visit(expressio2)
        elif comperador.getText() == '<=':
            return self.visit(expressio1) <= self.visit(expressio2)
        elif comperador.getText() == '>=':
            return self.visit(expressio1) >= self.visit(expressio2)
    
    def visitCrida_funcio(self, ctx):
        [_, _, Llista, _] = list(ctx.getChildren())
        print(len(Llista))

#input_stream = InputStream(input('? '))
input_stream = FileStream("input.txt")
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
  visitor = EvalVisitor()
  #visitor2 = TreeVisitor()
  #print('Result:')
  visitor.visit(tree)
  #print('\nTree:')
  #visitor2.visit(tree)
else:
  print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
  print(tree.toStringTree(recog=parser))