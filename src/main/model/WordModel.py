from model.IdentifierModel import IdentifierModel
from util.IdentifierSeparator import IdentifierSeparator

class WordModel():
    name: str = None
    frequency: int = None
    separated_words = None

    def __init__(self, identifier_model: IdentifierModel):
        self.name = identifier_model.get_name()
        self.frequency = 1
        self.separated_words = []
        self.separated_words = IdentifierSeparator(self.name).get_separated_identifier()

    def to_print(self):
        return {
            "frequency": self.frequency,
            "separated_words": self.separated_words
        }

    def to_csv(self, path, name):
        csv_line = [
            path + "/" + name,
            str(self.frequency),
            str(len(self.separated_words))
        ]
        return ";".join(csv_line) + "\n"

    def get_csv_header():
        csv_header = [
            "path",
            "frequency_per_file",
            "number_of_separated_words"
        ] 
        return ";".join(csv_header) + "\n"

    def get_name(self):
        return self.name
        
    def get_separated_words(self):
        return self.separated_words

    def increment_frequency(self):
        self.frequency = self.frequency + 1
    
 