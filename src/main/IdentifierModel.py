from WordModel import WordModel

class IdentifierModel():
	classNames = None
	methodNames = None
	variableNames = None
	anyIdentifiers = None

	def __init__(self):
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

	def set_class_name(self, name: str):
		self.classNames.append(WordModel(name).get_separated_word_obj())

	def set_method_name(self, name: str):
		self.methodNames.append(WordModel(name).get_separated_word_obj())

	def set_variable_name(self, name: str):
		self.variableNames.append(WordModel(name).get_separated_word_obj())

	def set_any_identifier(self, name: str):
		self.anyIdentifiers.append(WordModel(name).get_separated_word_obj())
