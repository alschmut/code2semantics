from model.IdentifierType import IdentifierType

class IdentifierModel():
	name: str = None
	line: int = None
	type: IdentifierType = None

	def __init__(self, name: str, line: int, type: IdentifierType):
		self.name = name
		self.line = line
		self.type = type
	
	def to_print(self):
		return {
            "name": self.name,
			"type": self.type.value,
            "line": self.line
        }

	def get_name(self):
		return self.name

	def get_type(self):
		return self.type
