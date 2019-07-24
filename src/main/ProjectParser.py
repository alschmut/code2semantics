import sys, os, time, json

sys.path.append(os.path.join(os.path.dirname(__file__), 'fileParser'))

from antlr4 import InputStream
from LanguageParser import LanguageParser
from Language import Language
from model.ProjectModel import ProjectModel
from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel
from model.FileParserModel import FileParserModel
from model.ProjectParserModel import ProjectParserModel
from util.FileOpener import FileOpener
from util.Timer import Timer

def get_project_name(is_file: bool, is_dir: bool, path: str):
	file_name: str = path.split("/")[-1]
	if is_file:
		return "".join(file_name.split(".")[:-1])
	elif is_dir:
		return file_name

def parse(is_file: bool, is_dir: bool, path: str):
	project_name = get_project_name(is_file, is_dir, path)
	if is_file:
		print(f'[+] Parse file "{project_name}"')
		project_parser_model = ProjectParserModel(path, project_name)
		project_parser_model.parse_file()
		project_parser_model.save_file_as_json()

	elif is_dir:
		print(f'[+] Parse all supported files in directory "{project_name}"')
		project_parser_model = ProjectParserModel(path, project_name)
		project_parser_model.traverse_directory()
		project_parser_model.save_file_as_json()

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		return

	path = os.path.abspath(sys.argv[1])
	is_file = os.path.isfile(path)
	is_dir = os.path.isdir(path)

	if is_file or is_dir:
		timer = Timer()
		parse(is_file, is_dir, path)
		print(f"[+] Finished: {timer.get_duration()}s")
	else: 
		print(f'[-] Could not find file or directory: "{path}"')

if __name__ == '__main__':
    main()
