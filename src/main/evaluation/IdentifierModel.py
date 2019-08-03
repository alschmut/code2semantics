
class IdentifierModel():
	usefulness: str = None
	numeric: str = None

	def __init__(self, identifier):
		self.numeric = identifier.get("numeric")
		self.usefulness = identifier.get("usefulness")

	def to_print(self):
		return {
			"usefulness": self.usefulness,
			"numeric": self.numeric
		}
