# Generated from exprs.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,4,1,12,8,1,
        11,1,12,1,13,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,3,1,3,1,3,3,3,39,8,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,9,
        3,1,3,0,1,6,4,0,2,4,6,0,2,1,0,9,10,1,0,11,12,63,0,8,1,0,0,0,2,11,
        1,0,0,0,4,33,1,0,0,0,6,38,1,0,0,0,8,9,3,2,1,0,9,1,1,0,0,0,10,12,
        3,4,2,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,
        14,3,1,0,0,0,15,16,5,14,0,0,16,17,5,1,0,0,17,34,3,6,3,0,18,19,5,
        2,0,0,19,34,3,6,3,0,20,21,5,3,0,0,21,22,3,6,3,0,22,23,5,4,0,0,23,
        24,3,2,1,0,24,25,5,5,0,0,25,34,1,0,0,0,26,27,5,6,0,0,27,28,3,6,3,
        0,28,29,5,7,0,0,29,30,3,2,1,0,30,31,5,5,0,0,31,34,1,0,0,0,32,34,
        5,17,0,0,33,15,1,0,0,0,33,18,1,0,0,0,33,20,1,0,0,0,33,26,1,0,0,0,
        33,32,1,0,0,0,34,5,1,0,0,0,35,36,6,3,-1,0,36,39,5,13,0,0,37,39,5,
        14,0,0,38,35,1,0,0,0,38,37,1,0,0,0,39,54,1,0,0,0,40,41,10,6,0,0,
        41,42,5,8,0,0,42,53,3,6,3,6,43,44,10,5,0,0,44,45,7,0,0,0,45,53,3,
        6,3,6,46,47,10,4,0,0,47,48,7,1,0,0,48,53,3,6,3,5,49,50,10,3,0,0,
        50,51,5,18,0,0,51,53,3,6,3,4,52,40,1,0,0,0,52,43,1,0,0,0,52,46,1,
        0,0,0,52,49,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,
        7,1,0,0,0,56,54,1,0,0,0,5,13,33,38,52,54
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'write'", "'if'", "'then'", "'end'", 
                     "'while'", "'do'", "'^'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "VAR", "VARS", "VARS2", "NOM", 
                      "CMP", "WS" ]

    RULE_root = 0
    RULE_lines = 1
    RULE_line = 2
    RULE_expr = 3

    ruleNames =  [ "root", "lines", "line", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NUM=13
    VAR=14
    VARS=15
    VARS2=16
    NOM=17
    CMP=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lines(self):
            return self.getTypedRuleContext(exprsParser.LinesContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.lines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.LineContext)
            else:
                return self.getTypedRuleContext(exprsParser.LineContext,i)


        def getRuleIndex(self):
            return exprsParser.RULE_lines

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLines" ):
                return visitor.visitLines(self)
            else:
                return visitor.visitChildren(self)




    def lines(self):

        localctx = exprsParser.LinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lines)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.line()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 147532) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Define_varContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_var" ):
                return visitor.visitDefine_var(self)
            else:
                return visitor.visitChildren(self)


    class Crida_funcioContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOM(self):
            return self.getToken(exprsParser.NOM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrida_funcio" ):
                return visitor.visitCrida_funcio(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)

        def lines(self):
            return self.getTypedRuleContext(exprsParser.LinesContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(exprsParser.ExprContext,0)

        def lines(self):
            return self.getTypedRuleContext(exprsParser.LinesContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = exprsParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = exprsParser.Define_varContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(exprsParser.VAR)
                self.state = 16
                self.match(exprsParser.T__0)
                self.state = 17
                self.expr(0)
                pass
            elif token in [2]:
                localctx = exprsParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(exprsParser.T__1)
                self.state = 19
                self.expr(0)
                pass
            elif token in [3]:
                localctx = exprsParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.match(exprsParser.T__2)
                self.state = 21
                self.expr(0)
                self.state = 22
                self.match(exprsParser.T__3)
                self.state = 23
                self.lines()
                self.state = 24
                self.match(exprsParser.T__4)
                pass
            elif token in [6]:
                localctx = exprsParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(exprsParser.T__5)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(exprsParser.T__6)
                self.state = 29
                self.lines()
                self.state = 30
                self.match(exprsParser.T__4)
                pass
            elif token in [17]:
                localctx = exprsParser.Crida_funcioContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.match(exprsParser.NOM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PotenciaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPotencia" ):
                return visitor.visitPotencia(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(exprsParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class Multiplicacio_divisioContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicacio_divisio" ):
                return visitor.visitMultiplicacio_divisio(self)
            else:
                return visitor.visitChildren(self)


    class Suma_restaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma_resta" ):
                return visitor.visitSuma_resta(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(exprsParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BooleaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.ExprContext)
            else:
                return self.getTypedRuleContext(exprsParser.ExprContext,i)

        def CMP(self):
            return self.getToken(exprsParser.CMP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolea" ):
                return visitor.visitBoolea(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = exprsParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(exprsParser.NUM)
                pass
            elif token in [14]:
                localctx = exprsParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(exprsParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = exprsParser.PotenciaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 41
                        self.match(exprsParser.T__7)
                        self.state = 42
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = exprsParser.Multiplicacio_divisioContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 44
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = exprsParser.Suma_restaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = exprsParser.BooleaContext(self, exprsParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        self.match(exprsParser.CMP)
                        self.state = 51
                        self.expr(4)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




