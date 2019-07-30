from model.IdentifierListModel import IdentifierListModel

class BaseListener():
    identifiers = None

    def __init__(self):
        self.identifiers = IdentifierListModel()

    def get_identifiers(self):
        return self.identifiers