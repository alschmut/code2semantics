import sys, os, time, json
from model.ProjectModel import ProjectModel
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from util.PathValidator import PathValidator
from service import Word2VecModel

FILE_EXTENSION = ".c2s.json"

def parse(project_path: str):
	project_name = PathExtractor().get_file_name(project_path)
	Logger().info(f'Analyze "{project_name}"')
	project_model = ProjectModel(project_path)

	if PathValidator().is_valid_directories([project_path], True):
		project_model.traverse_directory()
	else:
		project_model.parse_file()
	FileOpener().save_file_as_json(project_model.to_print(), project_name + FILE_EXTENSION)

def main():
	script_name: str = PathExtractor().get_file_name(sys.argv[0])
	timer = Timer()
	
	if len(sys.argv) == 3:
		model_path = PathExtractor().get_absolute_path(sys.argv[2])
		if not PathValidator().is_valid_files([model_path]):
			return
		Word2VecModel.instance.set_model(model_path)
	
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		Logger().usage(f"python {script_name} <file_or_directory_path> [<word2vec.model>]")
		return

	project_path = PathExtractor().get_absolute_path(sys.argv[1])

	if PathValidator().is_valid_paths([project_path]):
		parse(project_path)
		Logger().finish_script(timer.get_duration(), script_name)

if __name__ == '__main__':
    main()
