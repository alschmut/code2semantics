from antlr4 import *
from Java9Lexer import Java9Lexer
from Java9Listener import Java9Listener
from Java9Parser import Java9Parser
from Java9Visitor import Java9Visitor
import sys

class IdentifierListener(Java9Listener):
	identifiers = []

	def getIdentifiers(self):
		return self.identifiers

	def enterNormalClassDeclaration(self, ctx):
		print("Class: %s" % ctx.identifier().getText())
		self.identifiers.append({"type": "Class", "name": ctx.identifier().getText()})
		
	def enterSuperclass(self, ctx):
		print("SuperClass: %s" % ctx.classType().identifier().getText())

	def enterNormalInterfaceDeclaration(self, ctx):
		print("Normal Interface: %s" % ctx.identifier().getText())

	def enterAnnotationTypeDeclaration(self, ctx):
		print("Annotation Interface: %s" % ctx.identifier().getText())
		
	def enterVariableDeclaratorId(self, ctx):
		print("Variable: %s" % ctx.identifier().getText())

	def enterMethodDeclarator(self, ctx):
		print("Method: %s" % ctx.identifier().getText())
		self.identifiers.append({"type": "Method", "name": ctx.identifier().getText()})
		
	def enterIdentifier(self, ctx):
		print("Identifier: %s" % ctx.getText())
		
		

class IdentifierVisitor(Java9Visitor):
	identifiers = []

	def visitNormalClassDeclaration(self, ctx:Java9Parser.NormalClassDeclarationContext):
		print("Class: %s" % ctx.identifier().getText())
		self.identifiers.append({"type": "Class", "name": ctx.identifier().getText()})
		self.visitChildren(ctx)
		return self.identifiers

	def visitMethodDeclaration(self, ctx:Java9Parser.MethodDeclarationContext):
		print("Method: %s" % ctx.identifier().getText())
		self.identifiers.append({"type": "Method", "name": ctx.identifier().getText()})
		self.visitChildren(ctx)
		return self.identifiers
		


def txtget(filename):
	try:
		# open file read-only, get file content and close
		with open(filename, 'r') as file:
			file_content = file.read()
			return file_content

	except Exception as err:
		print("Could not open file: ", type(err), ":", err)
		return None
	
def main():
	input_stream = InputStream(txtget("AJavaExample.java"))
	lexer = Java9Lexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = Java9Parser(stream)
	tree = parser.compilationUnit()
	#visitor = IdentifierVisitor()
	#identifiers = visitor.visit(tree)
	#print(identifiers)
	#return identifiers

	printer = IdentifierListener()
	walker = ParseTreeWalker()
	walker.walk(printer, tree)
	print(printer.getIdentifiers())

if __name__ == '__main__':
    main()
