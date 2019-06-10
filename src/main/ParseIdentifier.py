from antlr4 import *
import sys, os
from AllParser import AllParser

def get_supported_extensions():
	return ["java", "kt"]

def parseFile(file_extension, input_stream):
	if file_extension == "java":
		return AllParser.parseJava9File(None, input_stream)
	elif file_extension == "kt":
		return AllParser.parseKotlinFile(None, input_stream)

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

def printStatus(filepath):
	print(f"[+] Analyzing: {filepath}")

def printIdentifier(file_extension, identifier_data):
	print(f"    Extension: {file_extension}")
	print(f"    Keywords: {identifier_data.keywords}")
	identifier_data.identifier.printAll()

def parseFileIfSupported(filepath):
	file_extension = getFileExtension(filepath)
	if file_extension in get_supported_extensions():
		file_content = get_file_content(filepath)
		if file_content:
			printStatus(filepath)
			input_stream = InputStream(file_content)
			identifier_data = parseFile(file_extension, input_stream)
			printIdentifier(file_extension, identifier_data)		

def getFilePath(path, filename):
	return path + os.sep + filename

def traverseDirectory(directory_path):
	for basepath, directories, filenames in os.walk(directory_path):
		for filename in filenames:
			filepath = getFilePath(basepath, filename)
			parseFileIfSupported(filepath)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		test_dir = "/Users/alexandersch/Documents/Beruf/Master/7 Thesis/Antlr/test_directory/subdir1/subdir2"
		print(f'[-] Use default test directory "{test_dir}"')
		sys.argv.append(test_dir)

	path = sys.argv[1]

	if os.path.isdir(path):
		traverseDirectory(path)
	else:
		parseFileIfSupported(path)

if __name__ == '__main__':
    main()
