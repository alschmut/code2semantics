import sys, os, time, json

sys.path.append(os.path.join(os.path.dirname(__file__), 'fileParser'))

from antlr4 import InputStream
from LanguageParser import LanguageParser
from Language import Language
from model.IdentifierModel import IdentifierModel
from model.DictionaryModel import DictionaryModel
from util.FileOpener import FileOpener
from util.Timer import Timer

class FileParserModel():

	file_path: str = None
	supported_extensions: [str] = None
	file_name: str = None
	file_extension: str = None
	timer: Timer = None

	def __init__(self, file_path: str, supported_extensions: [int]):
		self.file_path = file_path
		self.supported_extensions = supported_extensions
		self.timer = Timer()
		self.file_name = file_path.split("/")[-1]
		self.file_extension = file_path.split(".")[-1]

	def parse_if_valid(self):
		if self.file_extension in self.supported_extensions:
			file_content = FileOpener().get_file_content(self.file_path)
			if file_content:
				return self.parse(file_content)

	def parse(self, file_content):
		self.print_analyzing()
		identifier_model: IdentifierModel = LanguageParser().parse_file(self.file_extension, file_content)
		dictionary_model: DictionaryModel = DictionaryModel(identifier_model)
		self.print_finished()
		return (identifier_model, dictionary_model)

	def print_analyzing(self):
		print(f"\r[+] Analyzing: {self.file_path}", end="")

	def print_finished(self):
		print(f"\r[+] Finished ({self.timer.get_duration()}s): {self.file_path}")
