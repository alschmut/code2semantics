from model.MetricModel import MetricModel
from model.MetricType import MetricType
from service import SpacyModel
from service import Word2VecModel
from service import StopWordModel

class SeparatedWordModel():

    vector = None
    lemmatized_word: str = None
    metrics: dict = None

    def __init__(self, name: str):
        self.metrics = {}
        self.metrics["frequency"] = MetricModel(MetricType.Absolute, 1)

        spacy_word = SpacyModel.instance.get_en_spacy_line(name)[0]

        self.lemmatized_word = spacy_word.lemma_

        is_stop_word_spacy = self.bool_to_float(spacy_word.is_stop)
        self.metrics["is_stop_word_spacy"] = MetricModel(MetricType.Relative, is_stop_word_spacy)

        is_stop_word_nltk = self.bool_to_float(self.lemmatized_word in StopWordModel.instance.get_stop_words_nltk())
        self.metrics["is_stop_word_nltk"] = MetricModel(MetricType.Relative, is_stop_word_nltk)
        
        is_stop_word_smart = self.bool_to_float(self.lemmatized_word in StopWordModel.instance.get_stop_words_smart())
        self.metrics["is_stop_word_smart"] = MetricModel(MetricType.Relative, is_stop_word_smart)

        if Word2VecModel.instance.exists():
            is_dictionary_word = Word2VecModel.instance.is_word_in_dictionary(self.lemmatized_word)
            self.metrics["is_dictionary_word"] = MetricModel(MetricType.Relative, is_dictionary_word)

            if self.metrics.get("is_dictionary_word").get_value():
                self.vector = Word2VecModel.instance.get_vector(self.lemmatized_word)

    def bool_to_float(self, value: bool):
        return 1 if value else 0

    def to_print(self):
        return {
            "lemmatized_word": self.lemmatized_word,            
            "metrics": {key: metric_model.to_print() for (key, metric_model) in self.metrics.items()},
        }

    def increment_frequency(self):
        self.metrics["frequency"].increment_value_by_1()

    def calculate_semantic_metrics(self):
        distance_to_class_name = Word2VecModel.instance.get_distance_to_class(self.lemmatized_word)
        self.metrics["distance_to_class_name"] = MetricModel(MetricType.Relative, distance_to_class_name)

        distance_to_file_context = Word2VecModel.instance.get_distance_to_file_context(self.lemmatized_word)
        self.metrics["distance_to_file_context"] = MetricModel(MetricType.Relative, distance_to_file_context)

