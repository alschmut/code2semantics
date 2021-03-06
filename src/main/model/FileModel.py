from model.IdentifierListModel import IdentifierListModel
from model.IdentifierDictionaryModel import IdentifierDictionaryModel
from model.WordDictionaryModel import WordDictionaryModel
from model.IdentifierType import IdentifierType
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from antlrParser.LanguageParser import LanguageParser
from service import Word2VecModel

class FileModel():
	relative_path: str = None
	identifier_list_model: IdentifierListModel = None
	identifier_dictionary_model: IdentifierDictionaryModel = None
	word_dictionary_model: WordDictionaryModel = None

	path: str = None
	supported_extensions: [str] = None
	file_name: str = None
	extension: str = None
	timer: Timer = None
	content: str = None

	def __init__(self, path: str, supported_extensions: [int]):
		self.timer = Timer()
		self.path = path
		self.relative_path = PathExtractor().get_relative_path(path)
		self.supported_extensions = supported_extensions
		self.file_name = PathExtractor().get_file_name(path)
		self.extension = PathExtractor().get_file_extension(self.file_name)

	def to_print(self):
		return {
			"relative_path": self.relative_path,
			"identifier_list": self.identifier_list_model.to_print(),
			"identifier_dictionary": self.identifier_dictionary_model.to_print(),
			"word_dictionary": self.word_dictionary_model.to_print()
		}

	def to_csv(self):
		content = [identifier.to_csv(self.relative_path, name) for (name, identifier) in self.identifier_dictionary_model.get_dictionary().items()]
		return "".join(content)

	def is_valid(self):
		if self.extension in self.supported_extensions:
			self.content = FileOpener().get_file_content(self.path)
			return True if self.content else False

	def parse(self):
		Logger().start_analyzing(self.relative_path)
		self.identifier_list_model = LanguageParser().parse_file(self.extension, self.content)
		self.identifier_dictionary_model = IdentifierDictionaryModel(self.identifier_list_model)
		self.word_dictionary_model = WordDictionaryModel(self.identifier_dictionary_model)
		if Word2VecModel.instance.exists():
			self.calculate_semantic_metrics()
		self.identifier_dictionary_model.set_word_metrics(self.word_dictionary_model.get_dictionary())
		Logger().finish_analyzing(self.timer.get_duration(), self.relative_path)

	def calculate_semantic_metrics(self):
		self.set_word2vec_class_name()
		self.set_word2vec_file_context_name()
		self.word_dictionary_model.calculate_semantic_metrics()

	def set_word2vec_class_name(self):
		class_identifiers: [str] = self.identifier_list_model.get_filtered_identfier_names(IdentifierType.Class)
		class_identifier_words: [str] = self.identifier_dictionary_model.get_filtered_words(class_identifiers)
		Word2VecModel.instance.set_class_name(class_identifier_words)

	def set_word2vec_file_context_name(self):
		file_context_words: [str] = self.word_dictionary_model.get_dictionary_keys()
		Word2VecModel.instance.set_file_context_name(file_context_words)
