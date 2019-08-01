from model.SpacyModel import SpacyModel
from service import Word2VecModel
from service import StopWordModel

class SeparatedWordModel():
    name: str = None
    frequency: int = None
    lemmatized_word: str = None
    is_spacy_stop_word: bool = None
    is_nltk_stop_word: bool = None
    is_dictionary_word: bool = None
    distance_to_class_name: float = None
    distance_to_file_context: float = None

    vector = None

    def __init__(self, name: str):
        self.name = name
        self.frequency = 1
        spacy_word = SpacyModel().get_en_spacy_line(name)[0]
        self.lemmatized_word = spacy_word.lemma_
        self.is_spacy_stop_word = spacy_word.is_stop
        self.is_nltk_stop_word = self.lemmatized_word in StopWordModel.instance.get_stop_words()
        
        if Word2VecModel.instance.exists():
            self.is_dictionary_word = Word2VecModel.instance.is_word_in_dictionary(self.lemmatized_word)
            if self.is_dictionary_word:
                self.vector = Word2VecModel.instance.get_vector(self.lemmatized_word)


    def get_lemmaized_word(self, name: str):
        return SpacyModel().get_en_spacy_line(name)[0].lemma_

    def get_is_dictionary_word(self):
        return self.is_dictionary_word

    def get_vector(self):
        return self.vector

    def to_print(self):
        return {
            "name": self.name,
            "frequency": self.frequency,
            "lemmatized_word": self.lemmatized_word,            
            "is_spacy_stop_word": self.is_spacy_stop_word,
            "is_nltk_stop_word": self.is_nltk_stop_word,
            "is_dictionary_word": self.is_dictionary_word,
            "distance_to_class_name": self.distance_to_class_name,
            "distance_to_file_context": self.distance_to_file_context
        }

    def increment_frequency(self):
        self.frequency = self.frequency + 1

    def calculate_semantic_distances(self, class_name_vector_word, file_context_vector_word):
        if self.is_dictionary_word:
            if class_name_vector_word is not None:
                self.distance_to_class_name = Word2VecModel.instance.get_distance(self.lemmatized_word, class_name_vector_word)
            if file_context_vector_word is not None:
                self.distance_to_file_context = Word2VecModel.instance.get_distance(self.lemmatized_word, file_context_vector_word)
