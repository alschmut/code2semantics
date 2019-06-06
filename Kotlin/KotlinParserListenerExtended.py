from .KotlinParserListener import KotlinParserListener
from .KotlinParser import KotlinParser
from BaseListener import BaseListener

class KotlinParserListenerExtended(KotlinParserListener, BaseListener):
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        self.setIdentifiers("Class", ctx.simpleIdentifier().getText())
	
    def enterMultiVariableDeclaration(self, ctx:KotlinParser.MultiVariableDeclarationContext):
        self.setIdentifiers("Variable", ctx.simpleIdentifier().getText())

    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        self.setIdentifiers("Method", ctx.identifier().getText())
		
    def enterSimpleIdentifier(self, ctx:KotlinParser.SimpleIdentifierContext):
        self.setIdentifiers("Identifier", ctx.getText())
