from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
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

class LanguageParser():

    def parse_java_file(self, input_stream: InputStream):
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()
        listener = JavaParserListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.get_identifiers()

    def parse_java9_file(self, input_stream: InputStream):
        lexer = Java9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java9Parser(stream)
        tree = parser.compilationUnit()
        listener = Java9ListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.get_identifiers()

    def parse_kotlin_file(self, input_stream: InputStream):
        lexer = KotlinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = KotlinParser(stream)
        tree = parser.kotlinFile()
        listener = KotlinParserListenerExtended()

        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.get_identifiers()

    def parse_file(self, file_extension: [str], input_stream: InputStream):
        if file_extension == Language.Java.value:
            return LanguageParser.parse_java_file(self, input_stream)
        elif file_extension == Language.Kotlin.value:
            return LanguageParser.parse_kotlin_file(self, input_stream)