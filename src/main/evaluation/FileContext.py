
class FileContext():
	class_name_describes_context: str = None
	numeric: str = None

	def __init__(self, file_context):
		self.class_name_describes_context = file_context.get("class_name_describes_context")
		self.numeric = file_context.get("numeric")

	def to_print(self):
		return {
			"class_name_describes_context": self.class_name_describes_context,
			"numeric": self.numeric
		}
