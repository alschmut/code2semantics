from antlr4 import *
import sys, os, time
from LanguageParser import LanguageParser
from WordExtractor import WordExtractor
from Language import Language

def get_file_content(file_name):
	try:
		with open(file_name, "r") as file:
			return file.read()
	except Exception as err:
		print(f"Could not open file: {type(err)}: {err}")
		return None

def get_file_extension(file_path):
	return file_path.split(".")[-1]

def get_supported_extensions():
	return [extension.value for extension in Language]

def print_analyzing(file_path):
	print(f"\r[+] Analyzing: {file_path}", end="")

def get_time_duration(start):
	end = time.time()
	return round(end - start, 2)

def print_finished(file_path, start):
	print(f"\r[+] Finished ({get_time_duration(start)}s): {file_path}")





def parse_file_if_supported(file_path):
	start = time.time()
	file_extension = get_file_extension(file_path)
	if file_extension in get_supported_extensions():
		file_content = get_file_content(file_path)
		if file_content:
			print_analyzing(file_path)
			input_stream = InputStream(file_content)
			parser_data = LanguageParser.parse_file(None, file_extension, input_stream)
			parser_data["identifier"] = WordExtractor.extract_multi_words(None, parser_data.get("identifier"))
			print_finished(file_path, start)
			return parser_data

def get_file_path(path, file_name):
	return path + os.sep + file_name

def traverse_directory(directory_path):
	parsed_files = {}
	for basepath, _, file_names in os.walk(directory_path):
		for file_name in file_names:
			file_path = get_file_path(basepath, file_name)
			parsed_file = parse_file_if_supported(file_path)
			if parsed_file:
				parsed_files[file_path] = parsed_file
	return parsed_files

def parse_file(file_path):
	parsed_file = {}
	parsed_file[file_path] = parse_file_if_supported(file_path)
	return parsed_file

def get_path_without_trailing_slash():
	path = sys.argv[1]
	if path[-1] == "/":
		path = path[:-1]
	return path

def save_file(parser_data):
	output_file_name = "parser.text"
	with open(output_file_name, 'w') as f:
		f.write(str(parser_data))

def parse(path):
	if os.path.isdir(path):
		save_file(traverse_directory(path))
	else:
		save_file(parse_file(path))

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		test_dir = "/Users/alexandersch/Documents/Beruf/Master/7 Thesis/Antlr/test_directory/subdir1/subdir2"
		print(f'[-] Use default test directory "{test_dir}"')
		sys.argv.append(test_dir)

	parse(get_path_without_trailing_slash())

if __name__ == '__main__':
    main()
