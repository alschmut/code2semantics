from model.WordModel import WordModel
from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel
from util.FileOpener import FileOpener
from util.Timer import Timer
from fileParser.LanguageParser import LanguageParser

class FileModel():
	path: str = None
	identifier_model: IdentifierModel = None
	dictionary_model: DictionaryModel = None
	supported_extensions: [str] = None
	file_name: str = None
	file_extension: str = None
	timer: Timer = None
	file_content: str = None

	def __init__(self, path: str, supported_extensions: [int]):
		self.path = path
		self.supported_extensions = supported_extensions
		self.timer = Timer()
		self.file_name = path.split("/")[-1]
		self.file_extension = path.split(".")[-1]

	def to_print(self):
		return {
			"path": self.path,
			"identifiers": self.identifier_model.to_print(),
			"dictionary": self.dictionary_model.to_print(),
		}

	def is_valid(self):
		if self.file_extension in self.supported_extensions:
			self.file_content = FileOpener().get_file_content(self.path)
			return True if self.file_content else False

	def parse(self):
		self.print_analyzing()
		self.identifier_model = LanguageParser().parse_file(self.file_extension, self.file_content)
		self.dictionary_model = DictionaryModel(self.identifier_model)
		self.print_finished()

	def print_analyzing(self):
		print(f"\r[+] Analyzing: {self.path}", end="")

	def print_finished(self):
		print(f"\r[+] Finished ({self.timer.get_duration()}s): {self.path}")
