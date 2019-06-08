from antlr4 import *
from BaseListener import BaseListener

from Java9.Java9Lexer import Java9Lexer
from Java9.Java9Parser import Java9Parser
from ExtendedListener.Java9ListenerExtended import Java9ListenerExtended

from Kotlin.KotlinLexer import KotlinLexer
from Kotlin.KotlinParser import KotlinParser
from ExtendedListener.KotlinParserListenerExtended import KotlinParserListenerExtended

class AllParser():
    def parseJava9File(self, input_stream):
        lexer = Java9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java9Parser(stream)
        tree = parser.compilationUnit()
        listener = Java9ListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = lexer.literalNames
        identifier = listener.getAllIdentifier()
        return IdentifierData(identifier, keywords)

    def parseKotlinFile(self, input_stream):
        lexer = KotlinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = KotlinParser(stream)
        tree = parser.kotlinFile()
        listener = KotlinParserListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = lexer.literalNames
        identifier = listener.getAllIdentifier()
        return IdentifierData(identifier, keywords)

class IdentifierData():
    identifier = {}
    keywords = []

    def __init__(self, identifier, keywords):
        self.identifier = identifier
        self.keywords = keywords



