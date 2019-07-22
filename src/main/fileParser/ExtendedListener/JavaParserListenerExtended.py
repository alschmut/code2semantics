from Java.JavaParserListener import JavaParserListener
from Java.JavaParser import JavaParser
from BaseListener import BaseListener

class JavaParserListenerExtended(JavaParserListener, BaseListener):
	def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		self.identifiers.set_class_name(ctx.IDENTIFIER().getText())
		
	def enterVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
		self.identifiers.set_variable_name(ctx.IDENTIFIER().getText())

	def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		self.identifiers.set_method_name(ctx.IDENTIFIER().getText())

	# function does not exist	
	#def enterIdentifier(self, ctx):
	#	self.identifiers.set_any_identifier(ctx.getText())