from model.RawIdentifierModel import RawIdentifierModel

class SeparatedWordModel():
    name: str = None
    is_stopword: bool = None
    is_in_word2vec_dictionary: bool = None

    def __init__(self, name: str):
        self.name = name


    def to_print(self):
        return {
            "name": self.name,
            "is_stopword": self.is_stopword,
            "is_in_word2vec_dictionary": self.is_in_word2vec_dictionary
        }