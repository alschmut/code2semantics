from model.WordModel import WordModel
from model.IdentifierListModel import IdentifierListModel
from model.IdentifierModel import IdentifierModel

class IdentifierDictionaryModel():
	dictionary: dict = None

	def __init__(self, identifier_list_model: IdentifierListModel):
		self.dictionary = {}
		self.create_dictionary(identifier_list_model)

	def to_print(self):
		return { name: word_model.to_print() for name, word_model in self.dictionary.items() }

	def get_dictionary(self):
		return self.dictionary

	def create_dictionary(self, identifier_list_model: IdentifierListModel):
		for identifier in identifier_list_model.get_identifiers():
			name = identifier.get_name()
			if self.dictionary.get(name) == None:
				self.dictionary[name] = WordModel(identifier)
			else:
				self.dictionary[name].increment_frequency()

