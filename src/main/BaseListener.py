from IdentifierModel import IdentifierModel

class BaseListener():
    identifiers = IdentifierModel()

    def get_identifiers(self):
        return self.identifiers