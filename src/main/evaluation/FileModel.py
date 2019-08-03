from evaluation.IdentifierModel import IdentifierModel
from evaluation.FileContext import FileContext

class FileModel():
	semantic_context_identifier = None
	method_names = None
	variable_names = None
	class_names = None
	file_context = None

	def __init__(self, file):
		self.semantic_context_identifier = {
			"first": file.get("semantic_context_identifier").get("first"),
			"second": file.get("semantic_context_identifier").get("second"),
			"third": file.get("semantic_context_identifier").get("third")
		}
		self.method_names = {key: IdentifierModel(value) for (key, value) in file.get("method_names").items()}
		self.variable_names = {key: IdentifierModel(value) for (key, value) in file.get("variable_names").items()}
		key = list(file.get("class_names").keys())[0]
		self.class_names = {key: IdentifierModel(file.get("class_names").get(key))}
		key2 = list(file.get("class_names").keys())[1]
		self.file_context = FileContext(file.get("class_names").get(key2))


	def to_print(self):
		return {
			"semantic_context_identifier": self.semantic_context_identifier,
			"method_names": {key: value.to_print() for (key, value) in self.method_names.items()},
			"variable_names": {key: value.to_print() for (key, value) in self.variable_names.items()},
			"class_names": {key: value.to_print() for (key, value) in self.class_names.items()},
			"file_context": self.file_context.to_print()
		}