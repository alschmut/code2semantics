from antlr4 import *
from Java9.Java9Lexer import Java9Lexer
from Java9.Java9Parser import Java9Parser
from Java9.Java9ListenerExtended import Java9ListenerExtended

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