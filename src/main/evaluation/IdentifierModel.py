from model.IdentifierType import IdentifierType

class IdentifierModel():
	name: str = None
	usefulness: str = None
	type: IdentifierType = None

	def __init__(self, identifier):
		self.name = identifier.get("name")
		self.usefulness = identifier.get("usefulness")
		self.type = IdentifierType(identifier.get("type"))

	def to_print(self):
		return {
			"name": self.name,
			"type": self.type.value,
			"usefulness": self.usefulness
		}
