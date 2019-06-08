class BaseListener():
	identifier = {
		"classNames":[],
		"methodNames": [],
		"variableNames": [],
		"anyIdentifiers": []
	}
	
	def getAllIdentifier(self):
		return self.identifier

	def setClassName(self, name):
		self.identifier["classNames"].append(name)

	def setMethodName(self, name):
		self.identifier["methodNames"].append(name)

	def setVariableName(self, name):
		self.identifier["variableNames"].append(name)

	def setAnyIdentifier(self, name):
		self.identifier["anyIdentifiers"].append(name)