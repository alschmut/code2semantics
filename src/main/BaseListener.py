class Identifiers():
	classNames = []
	methodNames = []
	variableNames = []
	anyIdentifiers = []
	
	def print_all(self):
		self.print("classNames", self.classNames)
		self.print("methodNames", self.methodNames)
		self.print("variableNames", self.variableNames)
		self.print("anyIdentifiers", self.anyIdentifiers)

	def print(self, name, values):
		print(f"    {name}: {values}")

class BaseListener():
	identifier = Identifiers()
	
	def get_all_identifier(self):
		return self.identifier

	def set_class_name(self, name):
		self.identifier.classNames.append(name)

	def set_method_name(self, name):
		self.identifier.methodNames.append(name)

	def set_variable_name(self, name):
		self.identifier.variableNames.append(name)

	def set_any_identifier(self, name):
		self.identifier.anyIdentifiers.append(name)