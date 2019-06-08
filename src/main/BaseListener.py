class Identifiers():
	classNames = []
	methodNames = []
	variableNames = []
	anyIdentifiers = []
	
	def printAll(self):
		self.print("classNames", self.classNames)
		self.print("methodNames", self.methodNames)
		self.print("variableNames", self.variableNames)
		self.print("anyIdentifiers", self.anyIdentifiers)

	def print(self, name, values):
		print(f"    {name}: {values}")

class BaseListener():
	identifier = Identifiers()
	
	def getAllIdentifier(self):
		return self.identifier

	def setClassName(self, name):
		self.identifier.classNames.append(name)

	def setMethodName(self, name):
		self.identifier.methodNames.append(name)

	def setVariableName(self, name):
		self.identifier.variableNames.append(name)

	def setAnyIdentifier(self, name):
		self.identifier.anyIdentifiers.append(name)