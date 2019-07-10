class ProjectModel():
	files = []
	
	def get_all_files(self):
		return self.files

	def add_file(self, path, identfier):
		self.files.append({
			"name": path,
			"identifiers": identfier
		})