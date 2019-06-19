from Java.JavaParserListener import JavaParserListener
from Java.JavaParser import JavaParser
from BaseListener import BaseListener

class JavaParserListenerExtended(JavaParserListener, BaseListener):
	def enterClassDeclaration(self, ctx:JavaParser.ClassDeclarationContext):
		self.set_class_name(ctx.IDENTIFIER().getText())
		
	def enterVariableDeclaratorId(self, ctx:JavaParser.VariableDeclaratorIdContext):
		self.set_variable_name(ctx.IDENTIFIER().getText())

	def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
		self.set_method_name(ctx.IDENTIFIER().getText())

	# function does not exist	
	#def enterIdentifier(self, ctx):
	#	self.set_any_identifier(ctx.getText())