from model.RawIdentifierModel import RawIdentifierModel
from model.SeparatedWordModel import SeparatedWordModel

class WordModel():
    name: str = None
    line_numbers: [int] = None
    separated_words = None

    def __init__(self, raw_identifier_model: RawIdentifierModel):
        self.init_data(raw_identifier_model)
        self.separate_identifier()

    def init_data(self, raw_identifier_model: RawIdentifierModel):
        self.name = raw_identifier_model.get_name()
        self.line_numbers = [raw_identifier_model.get_line()]
        self.separated_words = []

    def to_print(self):
        return {
            "line_numbers": self.line_numbers,
            "separated_words": self.separated_words
        }

    def get_separated_words(self):
        return self.separated_words

    def append_line_number(self, line_number: int):
        self.line_numbers.append(line_number)
    
    def separate_identifier(self):
        separated_word: str = self.name
        last_char = separated_word[0]
        index = 1
        while index < len(separated_word):
            current_char = separated_word[index]
            if last_char.islower() and current_char.isupper():
                separated_word = self.insert_underscore(separated_word, index)
                index += 1

            if last_char.isupper() and current_char.islower():
                separated_word = self.insert_underscore_before(separated_word, index)
                index += 1

            index += 1
            last_char = current_char
        self.split_word_at_underscores(separated_word)

    def insert_underscore(self, separated_word, index):
        return separated_word[:index] + "_" + separated_word[index:]

    def insert_underscore_before(self, separated_word, index):
        return separated_word[:index - 1] + "_" + separated_word[index - 1:]

    def split_word_at_underscores(self, separated_words):
        self.separated_words = [word for word in separated_words.lower().split("_") if len(word) > 0]