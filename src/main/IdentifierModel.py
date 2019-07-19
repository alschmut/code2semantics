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

	def get_word_list(self):
		word_list = []
		identifiers = self.get_all_identifiers()
		for type in identifiers:
			for word_obj in identifiers.get(type):
				for word in word_obj.get("partial"):
					word_list.append(word)
		return word_list

	def get_word_dictionary(self):
		dictionary = {}
		for word in self.get_word_list():
			if dictionary.get(word) == None:
				dictionary[word] =  1
			else:
				dictionary[word] = dictionary.get(word) + 1
		return dictionary

	def set_class_name(self, name: str):
		self.classNames.append(WordModel(name).get_separated_word_obj())

	def set_method_name(self, name: str):
		self.methodNames.append(WordModel(name).get_separated_word_obj())

	def set_variable_name(self, name: str):
		self.variableNames.append(WordModel(name).get_separated_word_obj())

	def set_any_identifier(self, name: str):
		self.anyIdentifiers.append(WordModel(name).get_separated_word_obj())
