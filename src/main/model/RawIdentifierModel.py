class RawIdentifierModel():
	name = None
	line = None

	def __init__(self, name: str, line: int):
		self.name = name
		self.line = line
	
	def to_print(self):
		return {
            "name": self.name,
            "line": self.line,
        }

	def get_name(self):
		return self.name
	
	def get_line(self):
		return self.line
