
import os
from LanguageParser import LanguageParser
from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel
from model.FileModel import FileModel
from model.FileParserModel import FileParserModel

class ProjectModel():
	files: [] = None
	project_path: str = None
	supported_extensions: [int] = None
	project_name: str = None
	output_file_name: str = None

	def __init__(self, project_path: str, project_name: str):
		self.files = []
		self.project_path = project_path
		self.supported_extensions = LanguageParser().get_supported_extensions()
		self.project_name = project_name


	def to_print(self):
		return [file.to_print() for file in self.files]

	def add_file(self, path, identifier_model: IdentifierModel, dictionary_model: DictionaryModel):
		self.files.append(FileModel(path, identifier_model, dictionary_model))

	def traverse_directory(self):
		for base_path, _, file_names in os.walk(self.project_path):
			for file_name in file_names:
				file_path = self.get_absolute_file_path(base_path, file_name)
				file_parser_model = FileParserModel(file_path, self.supported_extensions)
				identifier_model, dictionary_model = file_parser_model.parse_if_valid()
				if identifier_model and dictionary_model:
					self.add_file(file_path, identifier_model, dictionary_model)

	def parse_file(self):
		file_parser_model = FileParserModel(self.project_path, self.supported_extensions)
		identifier_model, dictionary_model = file_parser_model.parse_if_valid()
		self.add_file(self.project_path, identifier_model, dictionary_model)

	def get_absolute_file_path(self, base_path: str, file_name: str):
		return base_path + os.sep + file_name