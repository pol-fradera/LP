# Generated from lc.g4 by ANTLR 4.13.0
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
        4,1,9,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,3,0,11,8,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,1,1,1,
        1,1,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,2,1,2,1,2,1,2,1,3,4,3,42,
        8,3,11,3,12,3,43,1,3,0,1,2,4,0,2,4,6,0,1,1,0,7,8,48,0,10,1,0,0,0,
        2,24,1,0,0,0,4,36,1,0,0,0,6,41,1,0,0,0,8,11,3,2,1,0,9,11,3,4,2,0,
        10,8,1,0,0,0,10,9,1,0,0,0,11,1,1,0,0,0,12,13,6,1,-1,0,13,14,5,1,
        0,0,14,15,3,2,1,0,15,16,5,2,0,0,16,25,1,0,0,0,17,18,5,5,0,0,18,19,
        3,6,3,0,19,20,5,3,0,0,20,21,3,2,1,3,21,25,1,0,0,0,22,25,5,4,0,0,
        23,25,7,0,0,0,24,12,1,0,0,0,24,17,1,0,0,0,24,22,1,0,0,0,24,23,1,
        0,0,0,25,33,1,0,0,0,26,27,10,6,0,0,27,28,5,8,0,0,28,32,3,2,1,7,29,
        30,10,4,0,0,30,32,3,2,1,5,31,26,1,0,0,0,31,29,1,0,0,0,32,35,1,0,
        0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,3,1,0,0,0,35,33,1,0,0,0,36,37,
        7,0,0,0,37,38,5,6,0,0,38,39,3,2,1,0,39,5,1,0,0,0,40,42,5,4,0,0,41,
        40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,7,1,0,0,
        0,5,10,24,31,33,43
    ]

class lcParser ( Parser ):

    grammarFileName = "lc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LLETRA", "LAMBDA", "EQUIVALENCIA", "MACRO", "MACRO_INF", 
                      "WS" ]

    RULE_root = 0
    RULE_terme = 1
    RULE_definir_macro = 2
    RULE_lletres = 3

    ruleNames =  [ "root", "terme", "definir_macro", "lletres" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    LLETRA=4
    LAMBDA=5
    EQUIVALENCIA=6
    MACRO=7
    MACRO_INF=8
    WS=9

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

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def definir_macro(self):
            return self.getTypedRuleContext(lcParser.Definir_macroContext,0)


        def getRuleIndex(self):
            return lcParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = lcParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 10
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.terme(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.definir_macro()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lcParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Terme_parContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerme_par" ):
                return visitor.visitTerme_par(self)
            else:
                return visitor.visitChildren(self)


    class MacroContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MACRO(self):
            return self.getToken(lcParser.MACRO, 0)
        def MACRO_INF(self):
            return self.getToken(lcParser.MACRO_INF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro" ):
                return visitor.visitMacro(self)
            else:
                return visitor.visitChildren(self)


    class LletraContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LLETRA(self):
            return self.getToken(lcParser.LLETRA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLletra" ):
                return visitor.visitLletra(self)
            else:
                return visitor.visitChildren(self)


    class AbstraccioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(lcParser.LAMBDA, 0)
        def lletres(self):
            return self.getTypedRuleContext(lcParser.LletresContext,0)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccio" ):
                return visitor.visitAbstraccio(self)
            else:
                return visitor.visitChildren(self)


    class Macro_infixaContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)

        def MACRO_INF(self):
            return self.getToken(lcParser.MACRO_INF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_infixa" ):
                return visitor.visitMacro_infixa(self)
            else:
                return visitor.visitChildren(self)


    class AplicacioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lcParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lcParser.TermeContext)
            else:
                return self.getTypedRuleContext(lcParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacio" ):
                return visitor.visitAplicacio(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lcParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = lcParser.Terme_parContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(lcParser.T__0)
                self.state = 14
                self.terme(0)
                self.state = 15
                self.match(lcParser.T__1)
                pass
            elif token in [5]:
                localctx = lcParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(lcParser.LAMBDA)
                self.state = 18
                self.lletres()
                self.state = 19
                self.match(lcParser.T__2)
                self.state = 20
                self.terme(3)
                pass
            elif token in [4]:
                localctx = lcParser.LletraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(lcParser.LLETRA)
                pass
            elif token in [7, 8]:
                localctx = lcParser.MacroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = lcParser.Macro_infixaContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                        self.state = 26
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 27
                        self.match(lcParser.MACRO_INF)
                        self.state = 28
                        self.terme(7)
                        pass

                    elif la_ == 2:
                        localctx = lcParser.AplicacioContext(self, lcParser.TermeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        self.terme(5)
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Definir_macroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUIVALENCIA(self):
            return self.getToken(lcParser.EQUIVALENCIA, 0)

        def terme(self):
            return self.getTypedRuleContext(lcParser.TermeContext,0)


        def MACRO(self):
            return self.getToken(lcParser.MACRO, 0)

        def MACRO_INF(self):
            return self.getToken(lcParser.MACRO_INF, 0)

        def getRuleIndex(self):
            return lcParser.RULE_definir_macro

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinir_macro" ):
                return visitor.visitDefinir_macro(self)
            else:
                return visitor.visitChildren(self)




    def definir_macro(self):

        localctx = lcParser.Definir_macroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definir_macro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 37
            self.match(lcParser.EQUIVALENCIA)
            self.state = 38
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LletresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLETRA(self, i:int=None):
            if i is None:
                return self.getTokens(lcParser.LLETRA)
            else:
                return self.getToken(lcParser.LLETRA, i)

        def getRuleIndex(self):
            return lcParser.RULE_lletres

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLletres" ):
                return visitor.visitLletres(self)
            else:
                return visitor.visitChildren(self)




    def lletres(self):

        localctx = lcParser.LletresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_lletres)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.match(lcParser.LLETRA)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




