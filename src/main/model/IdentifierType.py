from enum import Enum

class IdentifierType(Enum):
	Class = "class"
	Method = "method"
	Variable = "variable"
	Any = "any"