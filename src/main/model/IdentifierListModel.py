from model.WordModel import WordModel
from model.IdentifierModel import IdentifierModel
from model.IdentifierType import IdentifierType

class IdentifierListModel():
	identifiers: [IdentifierModel] = None

	def __init__(self):
		self.identifiers = []
	
	def to_print(self):
		return {
            "class_names": self.get_filtered_identfiers(IdentifierType.Class),
            "method_names": self.get_filtered_identfiers(IdentifierType.Method),
			"variable_names": self.get_filtered_identfiers(IdentifierType.Variable),
			"any_identifiers": self.get_filtered_identfiers(IdentifierType.Any)
        }

	def get_filtered_identfiers(self, type: IdentifierType):
		return [obj.to_print() for obj in self.identifiers if obj.get_type() == type]

	def get_identifiers(self):
		return self.identifiers

	def set_class_name(self, name: str, line: int):
		self.identifiers.append(IdentifierModel(name, line, IdentifierType.Class))

	def set_method_name(self, name: str, line: int):
		self.identifiers.append(IdentifierModel(name, line, IdentifierType.Method))

	def set_variable_name(self, name: str, line: int):
		self.identifiers.append(IdentifierModel(name, line, IdentifierType.Variable))

	def set_any_identifier(self, name: str, line: int):
		self.identifiers.append(IdentifierModel(name, line, IdentifierType.Any))
