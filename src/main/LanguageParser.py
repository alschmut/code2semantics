import re
from antlr4 import *
from BaseListener import BaseListener
from Language import Language

from Java.JavaLexer import JavaLexer
from Java.JavaParser import JavaParser
from ExtendedListener.JavaParserListenerExtended import JavaParserListenerExtended

from Java9.Java9Lexer import Java9Lexer
from Java9.Java9Parser import Java9Parser
from ExtendedListener.Java9ListenerExtended import Java9ListenerExtended

from Kotlin.KotlinLexer import KotlinLexer
from Kotlin.KotlinParser import KotlinParser
from ExtendedListener.KotlinParserListenerExtended import KotlinParserListenerExtended

class LanguageParser(object):

    def parse_java_file(self, input_stream):
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()
        listener = JavaParserListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = LanguageParser.get_keywords(self, lexer)
        identifier = listener.get_all_identifier()
        return LanguageParser.combine_as_map(self, identifier, keywords)

    def parse_java9_file(self, input_stream):
        lexer = Java9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java9Parser(stream)
        tree = parser.compilationUnit()
        listener = Java9ListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = LanguageParser.get_keywords(self, lexer)
        identifier = listener.get_all_identifier()
        return LanguageParser.combine_as_map(self, identifier, keywords)

    def parse_kotlin_file(self, input_stream):
        lexer = KotlinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = KotlinParser(stream)
        tree = parser.kotlinFile()
        listener = KotlinParserListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        keywords = LanguageParser.get_keywords(self, lexer)
        identifier = listener.get_all_identifier()
        return LanguageParser.combine_as_map(self, identifier, keywords)

    def combine_as_map(self, identifier, keywords):
        return {
            "identifier": identifier,
            "keywords": keywords
        }

    def get_keywords(self, lexer):
        return [word.replace("'", "").replace('"', '') for word in lexer.literalNames if re.search('[a-zA-Z]', word)]

    def parse_file(self, file_extension, input_stream):
        if file_extension == Language.Java.value:
            return LanguageParser.parse_java_file(self, input_stream)
        elif file_extension == Language.Kotlin.value:
            return LanguageParser.parse_kotlin_file(self, input_stream)



