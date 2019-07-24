from model.WordModel import WordModel
from model.IdentifierModel import IdentifierModel
from model.RawIdentifierModel import RawIdentifierModel

class DictionaryModel():
	dictionary: dict = None

	def __init__(self, identifier_model: IdentifierModel):
		self.dictionary = {}
		self.create_dictionary(identifier_model)

	def to_print(self):
		return { name: word_model.to_print() for name, word_model in self.dictionary.items() }

	def create_dictionary(self, identifier_model: IdentifierModel):
		for raw_identifier in identifier_model.get_all_identifiers_as_list():
			name = raw_identifier.get_name()
			if self.dictionary.get(name) == None:
				self.dictionary[name] = WordModel(raw_identifier)
			else:
				self.dictionary[name].append_line_number(raw_identifier.get_line())

