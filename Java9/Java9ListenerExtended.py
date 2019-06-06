from .Java9Listener import Java9Listener
from BaseListener import BaseListener

class Java9ListenerExtended(Java9Listener, BaseListener):
	def enterNormalClassDeclaration(self, ctx):
		self.setIdentifiers("Class", ctx.identifier().getText())
		
	def enterSuperclass(self, ctx):
		self.setIdentifiers("SuperClass", ctx.classType().identifier().getText())

	def enterNormalInterfaceDeclaration(self, ctx):
		self.setIdentifiers("Normal Interface", ctx.identifier().getText())

	def enterAnnotationTypeDeclaration(self, ctx):
		self.setIdentifiers("Annotation Interface", ctx.identifier().getText())
		
	def enterVariableDeclaratorId(self, ctx):
		self.setIdentifiers("Variable", ctx.identifier().getText())

	def enterMethodDeclarator(self, ctx):
		self.setIdentifiers("Method", ctx.identifier().getText())
		
	def enterIdentifier(self, ctx):
		self.setIdentifiers("Identifier", ctx.getText())