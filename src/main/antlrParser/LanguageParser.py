from antlr4 import CommonTokenStream, ParseTreeWalker, InputStream
from antlrParser.Language import Language
from antlrParser.Language import Language

from antlrParser.Java.JavaLexer import JavaLexer
from antlrParser.Java.JavaParser import JavaParser
from antlrParser.ExtendedListener.JavaParserListenerExtended import JavaParserListenerExtended

from antlrParser.Java9.Java9Lexer import Java9Lexer
from antlrParser.Java9.Java9Parser import Java9Parser
from antlrParser.ExtendedListener.Java9ListenerExtended import Java9ListenerExtended

from antlrParser.Kotlin.KotlinLexer import KotlinLexer
from antlrParser.Kotlin.KotlinParser import KotlinParser
from antlrParser.ExtendedListener.KotlinParserListenerExtended import KotlinParserListenerExtended

class LanguageParser():

    def get_supported_extensions(self):
        return [extension.value for extension in Language]

    def walk(self, listener, tree):
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return listener.get_identifiers()

    def parse_java_file(self, input_stream: InputStream):
        lexer = JavaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()
        listener = JavaParserListenerExtended()
        return self.walk(listener, tree)

    def parse_java9_file(self, input_stream: InputStream):
        lexer = Java9Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = Java9Parser(stream)
        tree = parser.compilationUnit()
        listener = Java9ListenerExtended()
        return self.walk(listener, tree)

    def parse_kotlin_file(self, input_stream: InputStream):
        lexer = KotlinLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = KotlinParser(stream)
        tree = parser.kotlinFile()
        listener = KotlinParserListenerExtended()
        return self.walk(listener, tree)

    def parse_file(self, file_extension: [str], file_content: str):
        input_stream = InputStream(file_content)
        if file_extension == Language.Java.value:
            return LanguageParser.parse_java_file(self, input_stream)
        elif file_extension == Language.Kotlin.value:
            return LanguageParser.parse_kotlin_file(self, input_stream)