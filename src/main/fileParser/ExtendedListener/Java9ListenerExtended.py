from Java9.Java9Listener import Java9Listener
from BaseListener import BaseListener

class Java9ListenerExtended(Java9Listener, BaseListener):
	def enterNormalClassDeclaration(self, ctx):
		self.identifiers.set_class_name(ctx.identifier().getText())
		
	def enterVariableDeclaratorId(self, ctx):
		self.identifiers.set_variable_name(ctx.identifier().getText())

	def enterMethodDeclarator(self, ctx):
		self.identifiers.set_method_name(ctx.identifier().getText())
		
	def enterIdentifier(self, ctx):
		self.identifiers.set_any_identifier(ctx.getText())