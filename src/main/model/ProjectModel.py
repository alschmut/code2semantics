from model.IdentifierModel import IdentifierModel

class ProjectModel():
	files: [] = None
	
	def __init__(self):
		self.files = []
		
	def get_all_files(self):
		return self.files

	def add_file(self, path, identifiers: IdentifierModel):
		self.files.append({
			"name": path,
			"identifiers": identifiers.get_all_identifiers(),
			"dictionary": identifiers.get_word_dictionary(),
		})