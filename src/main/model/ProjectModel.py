from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel
from model.FileModel import FileModel

class ProjectModel():
	files: [] = None
	
	def __init__(self):
		self.files = []
		
	def to_print(self):
		return [file.to_print() for file in self.files]

	def add_file(self, path, identifier_model: IdentifierModel, dictionary_model: DictionaryModel):
		self.files.append(FileModel(path, identifier_model, dictionary_model))