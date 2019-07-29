import sys, os, time, json
from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener
from util.Timer import Timer
from service import Word2VecModel

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
	if len(sys.argv) != 3:
		print(f'[-] Usage: python {sys.argv[0]} <file_or_directory_path> <word2vec.model>')
		return

	project_path = os.path.abspath(sys.argv[1])
	model_path = os.path.abspath(sys.argv[2])
	is_file = os.path.isfile(project_path)
	is_dir = os.path.isdir(project_path)
	is_model_file = os.path.isfile(model_path)

	if (is_file or is_dir) and is_model_file:
		timer = Timer()
		Word2VecModel.instance.set_model(model_path)
		parse(is_file, is_dir, project_path)
		print(f"[+] Finished: {timer.get_duration()}s")
	else: 
		print(f'[-] Could not find file or directory: "{project_path}"')

if __name__ == '__main__':
    main()
