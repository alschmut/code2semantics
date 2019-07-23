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
	
	def to_print(self):
		return {
            "classNames": self.classNames,
            "methodNames": self.methodNames,
			"variableNames": self.variableNames,
			"anyIdentifiers": self.anyIdentifiers
        }

	def get_word_dictionary(self):
		return self.dictionary

	def set_class_name(self, name: str, line: int):
		self.classNames.append({"name": name, "line": line})

	def set_method_name(self, name: str, line: int):
		self.methodNames.append({"name": name, "line": line})

	def set_variable_name(self, name: str, line: int):
		self.variableNames.append({"name": name, "line": line})

	def set_any_identifier(self, name: str, line: int):
		self.anyIdentifiers.append({"name": name, "line": line})
