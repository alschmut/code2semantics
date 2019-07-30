from model.RawIdentifierModel import RawIdentifierModel
from model.SpacyModel import SpacyModel
from service import Word2VecModel
from service import StopWordModel
from gensim.models import Word2Vec

class SeparatedWordModel():
    name: str = None
    lemmatized_word: str = None
    is_stop_word: bool = None
    is_in_word2vec_dictionary: bool = None

    def __init__(self, name: str):
        self.name = name
        self.lemmatized_word = self.get_lemmaized_word(name)
        self.is_stop_word = name in StopWordModel.instance.get_stop_words()
        if Word2VecModel.instance.exists():
            self.is_in_word2vec_dictionary = Word2VecModel.instance.is_word_in_dictionary(name)

    def get_lemmaized_word(self, name: str):
        return SpacyModel().get_en_spacy_line(name)[0].lemma_

    def to_print(self):
        return {
            "name": self.name,
            "lemmatized_word": self.lemmatized_word,
            "is_stop_word": self.is_stop_word,
            "is_in_word2vec_dictionary": self.is_in_word2vec_dictionary
        }