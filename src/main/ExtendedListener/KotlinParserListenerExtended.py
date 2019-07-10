from Kotlin.KotlinParserListener import KotlinParserListener
from Kotlin.KotlinParser import KotlinParser
from BaseListener import BaseListener

class KotlinParserListenerExtended(KotlinParserListener, BaseListener):
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        self.identifiers.set_class_name(ctx.simpleIdentifier().getText())
	
    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        self.identifiers.set_method_name(ctx.identifier().getText())

    def enterMultiVariableDeclaration(self, ctx:KotlinParser.MultiVariableDeclarationContext):
        self.identifiers.set_variable_name(ctx.simpleIdentifier().getText())
		
    def enterSimpleIdentifier(self, ctx:KotlinParser.SimpleIdentifierContext):
        self.identifiers.set_any_identifier(ctx.getText())
