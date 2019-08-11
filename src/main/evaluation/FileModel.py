from evaluation.IdentifierModel import IdentifierModel
from evaluation.ContextIdentifier import ContextIdentifier

class FileModel():
	semantic_context_identifier = None
	class_name_describes_context = None
	identifier_list: [] = None

	def __init__(self, file):
		self.semantic_context_identifier = ContextIdentifier(file.get("semantic_context_identifier"))
		self.class_name_describes_context = file.get("class_name_describes_context")
		self.identifier_list = [IdentifierModel(identifier) for identifier in file.get("identifier_list")]

	def to_print(self):
		return {
			"semantic_context_identifier": self.semantic_context_identifier.to_print(),
			"class_name_describes_context": self.class_name_describes_context,
			"identifier_list": [identifier.to_print() for identifier in self.identifier_list],
		}