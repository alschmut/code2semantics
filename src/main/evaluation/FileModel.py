from evaluation.IdentifierModel import IdentifierModel
from evaluation.FileContext import FileContext
from evaluation.ContextIdentifier import ContextIdentifier

class FileModel():
	semantic_context_identifier = None
	file_context = None
	class_names = None
	method_names = None
	variable_names = None

	def __init__(self, file):
		self.semantic_context_identifier = ContextIdentifier(file.get("semantic_context_identifier"))
		self.file_context = FileContext(file.get("file_context"))
		self.class_names = {key: IdentifierModel(value) for (key, value) in file.get("class_names").items()}
		self.method_names = {key: IdentifierModel(value) for (key, value) in file.get("method_names").items()}
		self.variable_names = {key: IdentifierModel(value) for (key, value) in file.get("variable_names").items()}

	def to_print(self):
		return {
			"semantic_context_identifier": self.semantic_context_identifier.to_print(),
			"file_context": self.file_context.to_print(),
			"class_names": {key: value.to_print() for (key, value) in self.class_names.items()},
			"method_names": {key: value.to_print() for (key, value) in self.method_names.items()},
			"variable_names": {key: value.to_print() for (key, value) in self.variable_names.items()}
		}