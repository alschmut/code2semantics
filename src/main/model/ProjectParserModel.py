import sys, os, time, json

sys.path.append(os.path.join(os.path.dirname(__file__), 'fileParser'))

from antlr4 import InputStream
from LanguageParser import LanguageParser
from model.ProjectModel import ProjectModel
from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel
from model.FileParserModel import FileParserModel
from util.FileOpener import FileOpener
from util.Timer import Timer

class ProjectParserModel():

	project_path: str = None
	supported_extensions: [int] = None
	project_name: str = None
	output_file_name: str = None
	project_model: ProjectModel = None

	def __init__(self, project_path: str, project_name: str):
		self.project_path = project_path
		self.supported_extensions = LanguageParser().get_supported_extensions()
		self.project_name = project_name
		self.output_file_name = f"{project_name}.json"
		self.project_model = ProjectModel()

	def traverse_directory(self):
		for base_path, _, file_names in os.walk(self.project_path):
			for file_name in file_names:
				file_path = self.get_absolute_file_path(base_path, file_name)
				file_parser_model = FileParserModel(file_path, self.supported_extensions)
				identifier_model, dictionary_model = file_parser_model.parse_if_valid()
				if identifier_model and dictionary_model:
					self.project_model.add_file(file_path, identifier_model, dictionary_model)

	def parse_file(self):
		file_parser_model = FileParserModel(self.project_path, self.supported_extensions)
		identifier_model, dictionary_model = file_parser_model.parse_if_valid()
		self.project_model.add_file(self.project_path, identifier_model, dictionary_model)

	def get_absolute_file_path(self, base_path: str, file_name: str):
		return base_path + os.sep + file_name

	def save_file_as_json(self):
		with open(self.output_file_name, 'w') as f:
			f.write(json.dumps(self.project_model.to_print()))
