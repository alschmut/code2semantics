from model.WordModel import WordModel
from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel

class FileModel():
	path: str = None
	identifier_model: IdentifierModel = None
	dictionar_model: DictionaryModel = None

	def __init__(self, path: str, identifier_model: IdentifierModel, dictionary_model: DictionaryModel):
		self.path = path
		self.identifier_model = identifier_model
		self.dictionar_model = dictionary_model

	def to_print(self):
		return {
			"path": self.path,
			"identifiers": self.identifier_model.to_print(),
			"dictionary": self.dictionar_model.to_print(),
		}

