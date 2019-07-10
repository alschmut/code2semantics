from IdentifierModel import IdentifierModel

class BaseListener():
    identifiers = None

    def __init__(self):
        self.identifiers = IdentifierModel()

    def get_identifiers(self):
        return self.identifiers