from model.IdentifierModel import IdentifierModel
from model.MetricModel import MetricModel
from util.IdentifierSeparator import IdentifierSeparator

class WordModel():
    name: str = None
    frequency: int = None
    separated_words = None
    metrics = None

    def __init__(self, identifier_model: IdentifierModel):
        if identifier_model:
            self.name = identifier_model.get_name()
            self.frequency = 1
            self.separated_words = IdentifierSeparator(self.name).get_separated_identifier()
            self.metrics = {}

    def to_print(self):
        return {
            "frequency": self.frequency,
            "separated_words": self.separated_words,
            "metrics": {key: value for (key, value) in self.metrics.items()}
        }

    def to_csv(self, relative_path, name):
        path = relative_path + "/" + name
        csv_line = [
            len(self.name),
            self.frequency,
            len(self.separated_words),
        ]
        csv_line += [value for (key, value) in self.metrics.items()]
        csv_line_as_str = [str(line) for line in csv_line]
        return path + ";" + ";".join(csv_line_as_str) + "\n"

    def get_csv_header(self):
        csv_header = [
            "path",
            "identifier_length",
            "identifier_frequency_per_file",
            "number_of_separated_words"
        ] 
        csv_header += [str(key) for (key, value) in self.metrics.items()]
        return ";".join(csv_header) + "\n"

    def get_name(self):
        return self.name
        
    def get_separated_words(self):
        return self.separated_words

    def increment_frequency(self):
        self.frequency += 1

    def set_word_metrics(self, word_dictionary):
        metric_keys = word_dictionary.get(self.separated_words[0]).get_metrics().keys()
        for metric_key in metric_keys:
            number_of_valid_values = 0
            summarized_value = 0
            for word in self.separated_words:
                metric = word_dictionary.get(word).get_metric_by_key(metric_key)
                if metric.get_value() is not None:
                    number_of_valid_values += 1
                    summarized_value += metric.get_value()
            self.metrics[metric_key] = self.get_metric_value(metric, summarized_value, number_of_valid_values)

    def get_metric_value(self, metric: MetricModel, summarized_value: int, number_of_valid_values: int):
        if metric.is_absolute():
            return round(summarized_value, 0)
        elif metric.is_relative():
            return self.get_relative_vmetric_alue(number_of_valid_values, summarized_value)


    def get_relative_vmetric_alue(self, number_of_valid_values: int, summarized_value: int):
        MAX_VALUE = 100
        if number_of_valid_values is 0:
            return MAX_VALUE
        else:
            return int(round(summarized_value * MAX_VALUE / number_of_valid_values, 0))