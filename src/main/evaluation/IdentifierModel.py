from model.IdentifierType import IdentifierType

class IdentifierModel():
	name: str = None
	usefulness: str = None
	type: IdentifierType = None

	def __init__(self, name, identifier, type: IdentifierType):
		self.name = name
		self.usefulness = identifier.get("numeric")
		self.type = type

	def to_print(self):
		return {
			"name": self.name,
			"type": self.type.value,
			"usefulness": self.usefulness
		}
