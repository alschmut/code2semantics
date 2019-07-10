from antlr4 import InputStream
import sys, os, time
from LanguageParser import LanguageParser
from Language import Language
from ProjectModel import ProjectModel
import IdentifierModel

def get_file_content(file_name: str):
	try:
		with open(file_name, "r") as file:
			return file.read()
	except Exception as err:
		print(f"Could not open file: {type(err)}: {err}")
		return None

def get_file_extension(file_path: str):
	return file_path.split(".")[-1]

def get_supported_extensions():
	return [extension.value for extension in Language]

def print_analyzing(file_path: str):
	print(f"\r[+] Analyzing: {file_path}", end="")

def get_time_duration(start: float):
	end = time.time()
	return round(end - start, 2)

def print_finished(file_path: str, start: float):
	print(f"\r[+] Finished ({get_time_duration(start)}s): {file_path}")

def parse_file_if_supported(file_path: str):
	start: float = time.time()
	file_extension: str = get_file_extension(file_path)
	if file_extension in get_supported_extensions():
		file_content = get_file_content(file_path)
		if file_content:
			print_analyzing(file_path)
			input_stream = InputStream(file_content)
			identifiers: IdentifierModel = LanguageParser.parse_file(None, file_extension, input_stream)
			print_finished(file_path, start)
			return identifiers

def get_file_path(path: str, file_name: str):
	return path + os.sep + file_name

def traverse_directory(directory_path: str):
	project = ProjectModel()
	for basepath, _, file_names in os.walk(directory_path):
		for file_name in file_names:
			file_path = get_file_path(basepath, file_name)
			identifiers = parse_file_if_supported(file_path)
			if identifiers:
				project.add_file(file_path, identifiers)
	return project

def parse_file(file_path: str):
	project = ProjectModel()
	project.add_file(file_path, parse_file_if_supported(file_path))
	return project

def get_path_without_trailing_slash(path: str):
	if path[-1] == "/":
		path = path[:-1]
	return path

def save_file(project: ProjectModel):
	output_file_name = "project.json"
	with open(output_file_name, 'w') as f:
		f.write(str(project.get_all_files()))

def parse(is_file: bool, is_dir: bool, path: str):
	if is_file:
		print(f'[+] Parse file "{path}"')
		save_file(parse_file(path))

	elif is_dir:
		print(f'[+] Parse all supported files in directory "{path}"')
		save_file(traverse_directory(path))

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path>')
		return

	path = get_path_without_trailing_slash(sys.argv[1])
	start = time.time()
	is_file = os.path.isfile(path)
	is_dir = os.path.isdir(path)

	if is_file or is_dir:
		parse(is_file, is_dir, path)
		print(f"[+] Finished: {get_time_duration(start)}s")
	else: 
		print(f'[-] Could not find file or directory: "{path}"')

if __name__ == '__main__':
    main()
