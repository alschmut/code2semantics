from Java9.Java9Listener import Java9Listener
from BaseListener import BaseListener

class Java9ListenerExtended(Java9Listener, BaseListener):
	def enterNormalClassDeclaration(self, ctx):
		self.setClassName(ctx.identifier().getText())
		
	def enterVariableDeclaratorId(self, ctx):
		self.setVariableName(ctx.identifier().getText())

	def enterMethodDeclarator(self, ctx):
		self.setMethodName(ctx.identifier().getText())
		
	def enterIdentifier(self, ctx):
		self.setAnyIdentifier(ctx.getText())