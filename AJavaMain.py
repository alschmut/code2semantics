from antlr4 import *
from Java9Lexer import Java9Lexer
from Java9Listener import Java9Listener
from Java9Parser import Java9Parser
from Java9Visitor import Java9Visitor
import sys
import os

class IdentifierListener(Java9Listener):
	identifiers = []

	def getIdentifiers(self):
		return self.identifiers

	def setIdentifiers(self, type, name):
		self.identifiers.append({"type": type, "name": name})

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

def get_file_content(filename):
	with open(filename, "r") as file:
		file_content = file.read()
		return file_content
	
def parseFile(input_stream):
	lexer = Java9Lexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = Java9Parser(stream)
	tree = parser.compilationUnit()
	listener = IdentifierListener()
	walker = ParseTreeWalker()
	walker.walk(listener, tree)
	return listener.getIdentifiers()

def printIdentifier(identifiers):
	for identifier in sorted(identifiers, key=lambda k: k["type"]):
		print(identifier["type"] + ": " + identifier["name"])

def hasFileExtension(file, extension):
	return file.split(".")[-1] == extension

def traverseCurrentDir():
	for path, dirs, files in os.walk("/Users/alexandersch/Documents/Beruf/Master/7 Thesis/Antlr/java_test_dir"):
		for file in files:
			if hasFileExtension(file, "java"):
				filepath = path + os.sep + file
				file_content = get_file_content(filepath)
				input_stream = InputStream(file_content)
				identifiers = parseFile(input_stream)
				printIdentifier(identifiers)

def main():
	traverseCurrentDir()

if __name__ == '__main__':
    main()
