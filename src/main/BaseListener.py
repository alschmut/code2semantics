class BaseListener():
	classNames = []
	methodNames = []
	variableNames = []
	anyIdentifiers = []
	
	def get_all_identifier(self):
		return {
            "classNames": self.classNames,
            "methodNames": self.methodNames,
			"variableNames": self.variableNames,
			"anyIdentifiers": self.anyIdentifiers
        }

	def set_class_name(self, name):
		self.classNames.append(name)

	def set_method_name(self, name):
		self.methodNames.append(name)

	def set_variable_name(self, name):
		self.variableNames.append(name)

	def set_any_identifier(self, name):
		self.anyIdentifiers.append(name)