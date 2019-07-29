import sys, os, time, json
from model.ProjectModel import ProjectModel
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
	output_file_name = f"{project_name}.json"
	project_model = ProjectModel(path, project_name)

	if is_file:
		print(f'[+] Parse file "{project_name}"')
		project_model.parse_file()
	elif is_dir:
		print(f'[+] Parse all supported files in directory "{project_name}"')
		project_model.traverse_directory()
	
	FileOpener().save_file_as_json(project_model.to_print(), output_file_name)

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
