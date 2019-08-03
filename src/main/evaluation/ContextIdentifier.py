
class ContextIdentifier():
	one: str = None
	two: str = None
	three: str = None

	def __init__(self, semantic_context_identifier):
		self.one = semantic_context_identifier.get("one")
		self.two = semantic_context_identifier.get("two")
		self.three = semantic_context_identifier.get("three")

	def to_print(self):
		return {
			"one": self.one,
			"two": self.two,
			"three": self.three
		}