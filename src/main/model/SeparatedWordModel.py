from model.SpacyModel import SpacyModel
from service import Word2VecModel
from service import StopWordModel

class SeparatedWordModel():
    name: str = None
    lemmatized_word: str = None
    is_spacy_stop_word: bool = None
    is_nltk_stop_word: bool = None
    is_dictionary_word: bool = None
    distance_to_class_name: float = None
    distance_to_file_name: float = None

    vector = None

    def __init__(self, name: str):
        self.name = name
        spacy_word = SpacyModel().get_en_spacy_line(name)[0]
        self.lemmatized_word = spacy_word.lemma_
        self.is_spacy_stop_word = spacy_word.is_stop
        self.is_nltk_stop_word = self.lemmatized_word in StopWordModel.instance.get_stop_words()
        
        if Word2VecModel.instance.exists():
            self.is_dictionary_word = Word2VecModel.instance.is_word_in_dictionary(self.lemmatized_word)
            self.vector = Word2VecModel.instance.get_vector(self.lemmatized_word)


    def get_lemmaized_word(self, name: str):
        return SpacyModel().get_en_spacy_line(name)[0].lemma_

    def to_print(self):
        return {
            "name": self.name,
            "lemmatized_word": self.lemmatized_word,
            "is_nltk_stop_word": self.is_nltk_stop_word,
            "is_dictionary_word": self.is_dictionary_word
        }