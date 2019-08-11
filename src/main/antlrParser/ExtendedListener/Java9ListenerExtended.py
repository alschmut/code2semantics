from antlrParser.Java9.Java9Listener import Java9Listener
from antlrParser.BaseListener import BaseListener

class Java9ListenerExtended(Java9Listener, BaseListener):
	def enterNormalClassDeclaration(self, ctx):
		self.identifiers.set_class_name(ctx.identifier().getText(), ctx.start.line)
		
	def enterVariableDeclaratorId(self, ctx):
		self.identifiers.set_variable_name(ctx.identifier().getText(), ctx.start.line)

	def enterMethodDeclarator(self, ctx):
		self.identifiers.set_method_name(ctx.identifier().getText(), ctx.start.line)
		
	def enterIdentifier(self, ctx):
		self.identifiers.set_any_identifier(ctx.getText(), ctx.start.line)