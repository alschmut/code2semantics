from evaluation.IdentifierModel import IdentifierModel
from evaluation.FileContext import FileContext
from evaluation.ContextIdentifier import ContextIdentifier
from model.IdentifierType import IdentifierType

class FileModel():
	semantic_context_identifier = None
	class_name_describes_context = None
	identifier_list: [] = None

	def __init__(self, file):
		self.semantic_context_identifier = ContextIdentifier(file.get("semantic_context_identifier"))
		self.class_name_describes_context = file.get("file_context").get("numeric")
		self.identifier_list = []
		for (key, value) in file.get("class_names").items():
			self.identifier_list.append(IdentifierModel(key, value, IdentifierType.Class))

		for (key, value) in file.get("method_names").items():
			self.identifier_list.append(IdentifierModel(key, value, IdentifierType.Method))

		for (key, value) in file.get("variable_names").items():
			self.identifier_list.append(IdentifierModel(key, value, IdentifierType.Variable))

	def to_print(self):
		return {
			"semantic_context_identifier": self.semantic_context_identifier.to_print(),
			"class_name_describes_context": self.class_name_describes_context,
			"identifier_list": [identifier.to_print() for identifier in self.identifier_list],
		}