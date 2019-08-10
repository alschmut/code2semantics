from model.SpacyModel import SpacyModel
from service import Word2VecModel
from service import StopWordModel

class SeparatedWordModel():
    frequency: int = None
    lemmatized_word: str = None
    is_stop_word_spacy: bool = None
    is_stop_word_nltk: bool = None
    is_stop_word_smart: bool = None
    is_dictionary_word: bool = None
    distance_to_class_name: float = None
    distance_to_file_context: float = None

    vector = None

    def __init__(self, name: str):
        self.frequency = 1
        spacy_word = SpacyModel().get_en_spacy_line(name)[0]
        self.lemmatized_word = spacy_word.lemma_
        self.is_stop_word_spacy = spacy_word.is_stop
        self.is_stop_word_nltk = self.lemmatized_word in StopWordModel.instance.get_stop_words_nltk()
        self.is_stop_word_smart = self.lemmatized_word in StopWordModel.instance.get_stop_words_smart()

        if Word2VecModel.instance.exists():
            self.is_dictionary_word = Word2VecModel.instance.is_word_in_dictionary(self.lemmatized_word)
            if self.is_dictionary_word:
                self.vector = Word2VecModel.instance.get_vector(self.lemmatized_word)

    def get_is_dictionary_word(self):
        return self.is_dictionary_word

    def get_vector(self):
        return self.vector

    def to_print(self):
        return {
            "frequency": self.frequency,
            "lemmatized_word": self.lemmatized_word,            
            "is_stop_word_spacy": self.is_stop_word_spacy,
            "is_stop_word_nltk": self.is_stop_word_nltk,
            "is_stop_word_smart": self.is_stop_word_smart,
            "is_w2v_dictionary_word": self.is_dictionary_word,
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
