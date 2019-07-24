from model.WordModel import WordModel
from model.RawIdentifierModel import RawIdentifierModel

class IdentifierModel():
	class_names = None
	method_names = None
	variable_names = None
	any_identifiers = None

	def __init__(self):
		self.class_names = []
		self.method_names = []
		self.variable_names = []
		self.any_identifiers = []
	
	def to_print(self):
		return {
            "class_names": [obj.to_print() for obj in self.class_names],
            "method_names": [obj.to_print() for obj in self.method_names],
			"variable_names": [obj.to_print() for obj in self.variable_names],
			"any_identifiers": [obj.to_print() for obj in self.any_identifiers],
        }

	def to_object(self):
		return {
            "class_names": self.class_names,
            "method_names": self.method_names,
			"variable_names": self.variable_names,
			"any_identifiers": self.any_identifiers,
        }

	def get_all_identifiers_as_list(self):
		raw_identifier_list = []
		identifier_dict = self.to_object()
		for key in identifier_dict:
			for raw_identifier in identifier_dict.get(key):
				raw_identifier_list.append(raw_identifier)
		return raw_identifier_list

	def set_class_name(self, name: str, line: int):
		self.class_names.append(RawIdentifierModel(name, line))

	def set_method_name(self, name: str, line: int):
		self.method_names.append(RawIdentifierModel(name, line))

	def set_variable_name(self, name: str, line: int):
		self.variable_names.append(RawIdentifierModel(name, line))

	def set_any_identifier(self, name: str, line: int):
		self.any_identifiers.append(RawIdentifierModel(name, line))
