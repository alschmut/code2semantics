from .KotlinParserListener import KotlinParserListener
from .KotlinParser import KotlinParser
from BaseListener import BaseListener

class KotlinParserListenerExtended(KotlinParserListener, BaseListener):
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        self.setClassName(ctx.simpleIdentifier().getText())
	
    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        self.setMethodName(ctx.identifier().getText())

    def enterMultiVariableDeclaration(self, ctx:KotlinParser.MultiVariableDeclarationContext):
        self.setVariableName(ctx.simpleIdentifier().getText())
		
    def enterSimpleIdentifier(self, ctx:KotlinParser.SimpleIdentifierContext):
        self.setAnyIdentifier(ctx.getText())
