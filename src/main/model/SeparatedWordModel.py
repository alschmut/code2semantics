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
        self.metrics["word_frequency_per_file"] = MetricModel(MetricType.Absolute, 1)

        spacy_word = SpacyModel.instance.get_en_spacy_line(name)[0]

        self.lemmatized_word = spacy_word.lemma_

        if Word2VecModel.instance.exists():
            is_dictionary_word = Word2VecModel.instance.is_word_in_dictionary(self.lemmatized_word)
            self.metrics["percent_of_word2vec_words"] = MetricModel(MetricType.Relative, is_dictionary_word)

            if self.metrics.get("percent_of_word2vec_words").get_value():
                self.vector = Word2VecModel.instance.get_vector(self.lemmatized_word)

    def bool_to_int(self, value: bool):
        return 1 if value else 0

    def get_metrics(self):
        return self.metrics

    def get_metric_by_key(self, key):
        return self.metrics.get(key)

    def to_print(self):
        return {
            "lemmatized_word": self.lemmatized_word,            
            "metrics": {key: metric_model.to_print() for (key, metric_model) in self.metrics.items()},
        }

    def increment_frequency(self):
        self.metrics["word_frequency_per_file"].increment_value_by_1()

    def calculate_semantic_metrics(self):
        distance_to_class_name = Word2VecModel.instance.get_distance_to_class(self.lemmatized_word)
        self.metrics["distance_to_class_name"] = MetricModel(MetricType.Relative, distance_to_class_name)

        distance_to_file_context = Word2VecModel.instance.get_distance_to_file_context(self.lemmatized_word)
        self.metrics["distance_to_file_context"] = MetricModel(MetricType.Relative, distance_to_file_context)

