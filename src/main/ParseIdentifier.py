from antlr4 import *
import sys, os
from LanguageParser import LanguageParser
from WordExtractor import WordExtractor
from Language import Language

def get_file_content(filename):
	try:
		with open(filename, "r") as file:
			return file.read()
	except Exception as err:
		print(f"Could not open file: {type(err)}: {err}")
		return None

def get_file_extension(filepath):
	return filepath.split(".")[-1]

def print_status(filepath):
	print(f"[+] Analyzing: {filepath}")

def get_supported_extensions():
	return [extension.value for extension in Language]

def parse_file_if_supported(filepath):
	file_extension = get_file_extension(filepath)
	if file_extension in get_supported_extensions():
		file_content = get_file_content(filepath)
		if file_content:
			print_status(filepath)
			input_stream = InputStream(file_content)
			parser_data = LanguageParser.parse_file(None, file_extension, input_stream)
			extracted_data = WordExtractor.extract_multi_words(None, parser_data)
			print(extracted_data)

def get_file_path(path, filename):
	return path + os.sep + filename

def traverse_directory(directory_path):
	for basepath, directories, filenames in os.walk(directory_path):
		for filename in filenames:
			filepath = get_file_path(basepath, filename)
			parse_file_if_supported(filepath)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		test_dir = "/Users/alexandersch/Documents/Beruf/Master/7 Thesis/Antlr/test_directory/subdir1/subdir2"
		print(f'[-] Use default test directory "{test_dir}"')
		sys.argv.append(test_dir)

	path = sys.argv[1]

	if os.path.isdir(path):
		traverse_directory(path)
	else:
		parse_file_if_supported(path)

if __name__ == '__main__':
    main()
