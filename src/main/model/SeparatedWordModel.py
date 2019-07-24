import spacy
from model.RawIdentifierModel import RawIdentifierModel
from model.StopWordModel import StopWordModel
from nltk.corpus import stopwords

class SeparatedWordModel():
    name: str = None
    lemmatized_word: str = None
    is_stop_word: bool = None
    is_in_word2vec_dictionary: bool = None

    def __init__(self, name: str):
        self.name = name
        self.lemmatized_word = self.get_lemmaized_word(name)
        self.is_stop_word = name in StopWordModel().get_stop_words()

    def get_lemmaized_word(self, name: str):
        sp = spacy.load("en")
        return sp(name)[0].lemma_

    def to_print(self):
        return {
            "name": self.name,
            "lemmatized_word": self.lemmatized_word,
            "is_stop_word": self.is_stop_word,
            "is_in_word2vec_dictionary": self.is_in_word2vec_dictionary
        }