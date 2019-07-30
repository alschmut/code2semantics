from model.WordModel import WordModel
from model.IdentifierModel import IdentifierModel
from model.IdentifierDictionaryModel import IdentifierDictionaryModel
from model.WordDictionaryModel import WordDictionaryModel
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from fileParser.LanguageParser import LanguageParser

class FileModel():
	path: str = None
	identifier_model: IdentifierModel = None
	identifier_dictionary_model: IdentifierDictionaryModel = None
	word_dictionary_model: WordDictionaryModel = None
	supported_extensions: [str] = None
	file_name: str = None
	file_extension: str = None
	timer: Timer = None
	file_content: str = None

	def __init__(self, path: str, supported_extensions: [int]):
		self.timer = Timer()
		self.path = path
		self.supported_extensions = supported_extensions
		self.file_name = path.split("/")[-1]
		self.file_extension = path.split(".")[-1]

	def to_print(self):
		return {
			"path": self.path,
			"identifier_list": self.identifier_model.to_print(),
			"identifier_dictionary": self.identifier_dictionary_model.to_print(),
			"word_dictionary": self.word_dictionary_model.to_print(),

		}

	def is_valid(self):
		if self.file_extension in self.supported_extensions:
			self.file_content = FileOpener().get_file_content(self.path)
			return True if self.file_content else False

	def parse(self):
		Logger().start_analyzing(self.path)
		self.identifier_model = LanguageParser().parse_file(self.file_extension, self.file_content)
		self.identifier_dictionary_model = IdentifierDictionaryModel(self.identifier_model)
		self.word_dictionary_model = WordDictionaryModel(self.identifier_dictionary_model)
		Logger().finish_analyzing(self.timer.get_duration(), self.path)