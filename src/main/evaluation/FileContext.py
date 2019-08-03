
class FileContext():
	class_name_describes_context: str = None
	numeric: str = None

	def __init__(self, numeric):
		self.numeric = numeric
		self.class_name_describes_context = self.get_word(numeric)

	def to_print(self):
		return {
			"class_name_describes_context": self.class_name_describes_context,
			"numeric": self.numeric
		}

	def get_word(self, numeric):
		if numeric == 0:
			return "Not at all"
		elif numeric == 1:
			return "Slightly"
		elif numeric == 2:
			return "Moderately"
		elif numeric == 3:
			return "Very"
		elif numeric == 4:
			return "Extremely"
