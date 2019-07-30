from model.SeparatedWordModel import SeparatedWordModel
from model.DictionaryModel import DictionaryModel
from model.RawIdentifierModel import RawIdentifierModel

class WordDictionaryModel():
	word_dictionary: dict = None

	def __init__(self, dictionary_model: DictionaryModel):
		self.word_dictionary = {}
		self.create_dictionary(dictionary_model)

	def to_print(self):
		return { name: separated_word_model.to_print() for name, separated_word_model in self.word_dictionary.items() }

	def create_dictionary(self, dictionary_model: DictionaryModel):
		dictionary = dictionary_model.get_dictionary()
		for key in dictionary:
			for word in dictionary.get(key).get_separated_words():
				if self.word_dictionary.get(word) == None:
					self.word_dictionary[word] = SeparatedWordModel(word)