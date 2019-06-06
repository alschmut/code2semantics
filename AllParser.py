from antlr4 import *
from BaseListener import BaseListener

from Java9.Java9Lexer import Java9Lexer
from Java9.Java9Parser import Java9Parser
from Java9.Java9ListenerExtended import Java9ListenerExtended

from Kotlin.KotlinLexer import KotlinLexer
from Kotlin.KotlinParser import KotlinParser
from Kotlin.KotlinParserListenerExtended import KotlinParserListenerExtended

class AllParser():
    def parseJava9File(self, input_stream):
        lexer = Java9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java9Parser(stream)
        tree = parser.compilationUnit()
        listener = Java9ListenerExtended()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.getIdentifiers()

    def parseKotlinFile(self, input_stream):
        lexer = KotlinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = KotlinParser(stream)
        tree = parser.kotlinFile()
        listener = KotlinParserListenerExtended()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.getIdentifiers()