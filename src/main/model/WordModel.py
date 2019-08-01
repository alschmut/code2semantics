from model.IdentifierModel import IdentifierModel
from model.SeparatedWordModel import SeparatedWordModel

class WordModel():
    name: str = None
    frequency: int = None
    separated_words = None

    def __init__(self, identifier_model: IdentifierModel):
        self.name = identifier_model.get_name()
        self.frequency = 1
        self.separated_words = []
        self.separate_identifier()        

    def to_print(self):
        return {
            "frequency": self.frequency,
            "separated_words": self.separated_words
        }

    def get_name(self):
        return self.name
        
    def get_separated_words(self):
        return self.separated_words

    def increment_frequency(self):
        self.frequency = self.frequency + 1
    
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