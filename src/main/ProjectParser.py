import sys, os, time, json
from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.FileName import FileName
from util.PathValidator import PathValidator
from service import Word2VecModel

def parse_file(path: str, project_name: str):
	Logger().info(f'Parse file "{project_name}"')
	project_model = ProjectModel(path, project_name)
	project_model.parse_file()
	FileOpener().save_file_as_json(project_model.to_print(), project_name + ".json")

def parse_directory(path: str, project_name: str):
	Logger().info(f'Parse all supported files in directory "{project_name}"')
	project_model = ProjectModel(path, project_name)
	project_model.traverse_directory()
	FileOpener().save_file_as_json(project_model.to_print(), project_name + ".json")

def parse(project_path: str, model_path: str):
	Word2VecModel.instance.set_model(model_path)
	project_name = FileName().get_file_name(project_path)
	if PathValidator().is_valid_directories([project_path], True):
		parse_directory(project_path, project_name)
	else: 
		parse_file(project_path, project_name)

def main():
	script_name: str = FileName().get_file_name(sys.argv[0])

	if len(sys.argv) != 3:
		Logger().usage(f"python {script_name} <file_or_directory_path> <word2vec.model>")
		return

	project_path = FileName().get_absolute_path(sys.argv[1])
	model_path = FileName().get_absolute_path(sys.argv[2])

	if PathValidator().is_valid_paths([project_path]) and PathValidator().is_valid_files([model_path]):
		timer = Timer()
		parse(project_path, model_path)
		Logger().finish_script(timer.get_duration(), script_name)

if __name__ == '__main__':
    main()
