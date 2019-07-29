from fileParser.Kotlin.KotlinParserListener import KotlinParserListener
from fileParser.Kotlin.KotlinParser import KotlinParser
from fileParser.BaseListener import BaseListener

class KotlinParserListenerExtended(KotlinParserListener, BaseListener):
    def enterClassDeclaration(self, ctx:KotlinParser.ClassDeclarationContext):
        self.identifiers.set_class_name(ctx.simpleIdentifier().getText(), ctx.start.line)
	
    def enterFunctionDeclaration(self, ctx:KotlinParser.FunctionDeclarationContext):
        self.identifiers.set_method_name(ctx.identifier().getText(), ctx.start.line)

    def enterMultiVariableDeclaration(self, ctx:KotlinParser.MultiVariableDeclarationContext):
        self.identifiers.set_variable_name(ctx.simpleIdentifier().getText(), ctx.start.line)
		
    def enterSimpleIdentifier(self, ctx:KotlinParser.SimpleIdentifierContext):
        self.identifiers.set_any_identifier(ctx.getText(), ctx.start.line)
