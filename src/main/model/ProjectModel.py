from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel

class ProjectModel():
	files: [] = None
	
	def __init__(self):
		self.files = []
		
	def get_all_files(self):
		return self.files

	def add_file(self, path, identifier_list: IdentifierModel, dictionary: DictionaryModel):
		self.files.append({
			"name": path,
			"identifiers": identifier_list.to_print(),
			"dictionary": dictionary.to_print(),
		})