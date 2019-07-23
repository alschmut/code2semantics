from model.WordModel import WordModel
from model.IdentifierModel import IdentifierModel

class DictionaryModel():
	dictionary: dict = None

	def __init__(self, identifier_model: IdentifierModel):
		self.dictionary = {}
		self.create_dictionary(identifier_model)

	def to_print(self):
		return self.dictionary

	def create_dictionary(self, identifier_model: IdentifierModel):
		identifier_list = identifier_model.to_print()
		for type in identifier_list:
			for identifier in identifier_list.get(type):
				name = identifier.get("name")
				if self.dictionary.get(name) == None:
					self.dictionary[name] = WordModel(identifier).get_separated_word_obj()
				else:
					line = identifier.get("line")
					self.dictionary[name]["lineNumbers"].append(line)

