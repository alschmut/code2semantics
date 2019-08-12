from model.IdentifierModel import IdentifierModel
from model.MetricType import MetricType
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
        self.frequency = self.frequency + 1

    def set_word_metrics(self, word_dictionary):
        metric_keys = word_dictionary.get(self.separated_words[0]).to_print().get("metrics").keys()

        for metric_key in metric_keys:
            number_of_valid_distances = 0
            summarized_value = 0
            metric_type = None
            for word in self.separated_words:
                metric = word_dictionary.get(word).to_print().get("metrics").get(metric_key)
                value = metric.get("value")
                metric_type = metric.get("type")
                if value != None:
                    number_of_valid_distances += 1
                    summarized_value += value
            if metric_type is MetricType.Absolute:
                self.metrics[metric_key] = round(summarized_value, 0)
            else:
                if number_of_valid_distances is 0:
                    self.metrics[metric_key] = None
                else:
                    self.metrics[metric_key] = int(round(summarized_value * 100 / number_of_valid_distances, 0))