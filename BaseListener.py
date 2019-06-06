class BaseListener():
	identifiers = []

	def getIdentifiers(self):
		return self.identifiers

	def setIdentifiers(self, type, name):
		self.identifiers.append({"type": type, "name": name})