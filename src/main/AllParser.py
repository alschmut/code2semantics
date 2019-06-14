from antlr4 import *
from BaseListener import BaseListener
from Language import Language

from Java9.Java9Lexer import Java9Lexer
from Java9.Java9Parser import Java9Parser
from ExtendedListener.Java9ListenerExtended import Java9ListenerExtended

from Kotlin.KotlinLexer import KotlinLexer
from Kotlin.KotlinParser import KotlinParser
from ExtendedListener.KotlinParserListenerExtended import KotlinParserListenerExtended

class AllParser(object):
    def parse_java9_file(self, input_stream):
        lexer = Java9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java9Parser(stream)
        tree = parser.compilationUnit()
        listener = Java9ListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = lexer.literalNames
        identifier = listener.get_all_identifier()
        return AllParser.combine_as_map(self, identifier, keywords)

    def parse_kotlin_file(self, input_stream):
        lexer = KotlinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = KotlinParser(stream)
        tree = parser.kotlinFile()
        listener = KotlinParserListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = lexer.literalNames
        identifier = listener.get_all_identifier()
        return AllParser.combine_as_map(self, identifier, keywords)

    def combine_as_map(self, identifier, keywords):
        return {
            "identifier": identifier,
            "keywords": keywords
        }

    def parse_file(self, file_extension, input_stream):
        if file_extension == Language.Java.value:
            return AllParser.parse_java9_file(self, input_stream)
        elif file_extension == Language.Kotlin.value:
            return AllParser.parse_kotlin_file(self, input_stream)



