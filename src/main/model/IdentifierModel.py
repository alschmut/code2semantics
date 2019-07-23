from model.WordModel import WordModel

class IdentifierModel():
	dictionary = None
	classNames = None
	methodNames = None
	variableNames = None
	anyIdentifiers = None

	def __init__(self):
		self.dictionary = {}
		self.classNames = []
		self.methodNames = []
		self.variableNames = []
		self.anyIdentifiers = []
	
	def get_all_identifiers(self):
		return {
            "classNames": self.classNames,
            "methodNames": self.methodNames,
			"variableNames": self.variableNames,
			"anyIdentifiers": self.anyIdentifiers
        }

	def get_word_dictionary(self):
		return self.dictionary

	def extract_identifier(self):
		identifiers = self.get_all_identifiers()
		for type in identifiers:
			for identifier in identifiers.get(type):
				name = identifier.get("name")
				if self.dictionary.get(name) == None:
					self.dictionary[name] = WordModel(identifier).get_separated_word_obj()
				else:
					line = identifier.get("line")
					self.dictionary[name]["lineNumbers"].append(line)

	def set_class_name(self, name: str, line: int):
		self.classNames.append({"name": name, "line": line})

	def set_method_name(self, name: str, line: int):
		self.methodNames.append({"name": name, "line": line})

	def set_variable_name(self, name: str, line: int):
		self.variableNames.append({"name": name, "line": line})

	def set_any_identifier(self, name: str, line: int):
		self.anyIdentifiers.append({"name": name, "line": line})
