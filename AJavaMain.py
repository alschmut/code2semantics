from antlr4 import *
from Java9Lexer import Java9Lexer
from Java9Parser import Java9Parser
from Java9ListenerExtended import Java9ListenerExtended
import sys
import os

def get_supported_extensions():
	return ["java"]

def parseJava9File(input_stream):
	lexer = Java9Lexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = Java9Parser(stream)
	tree = parser.compilationUnit()
	listener = Java9ListenerExtended()
	walker = ParseTreeWalker()
	walker.walk(listener, tree)
	return listener.getIdentifiers()

def parseFile(file_extension, input_stream):
	if file_extension == "java":
		return parseJava9File(input_stream)

def get_file_content(filename):
	try:
		with open(filename, "r") as file:
			file_content = file.read()
			return file_content
	except Exception as err:
		print(f"Could not open file: {type(err)}: {err}")
		return None

def getFileExtension(filepath):
	return filepath.split(".")[-1]

def checkFileToParse(filepath):
	file_extension = getFileExtension(filepath)
	if file_extension in get_supported_extensions():
		file_content = get_file_content(filepath)
		if file_content:
			input_stream = InputStream(file_content)
			identifiers = parseFile(file_extension, input_stream)
			printIdentifier(identifiers)		
			
def printIdentifier(identifiers):
	for identifier in sorted(identifiers, key=lambda k: k["type"]):
		print(f'{identifier["type"]}: {identifier["name"]}')

def getFilePath(path, filename):
	return path + os.sep + filename

def traverseDirectory(directory_path):
	for basepath, directories, filenames in os.walk(directory_path):
		for filename in filenames:
			filepath = getFilePath(basepath, filename)
			checkFileToParse(filepath)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		test_dir = "/Users/alexandersch/Documents/Beruf/Master/7 Thesis/Antlr/java_test_dir/subdir1/subdir2/"
		print(f'[-] Use default test directory "{test_dir}"')
		sys.argv.append(test_dir)

	path = sys.argv[1]

	if os.path.isdir(path):
		traverseDirectory(path)
	else:
		checkFileToParse(path)

if __name__ == '__main__':
    main()
