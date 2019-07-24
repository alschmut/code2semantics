from model.RawIdentifierModel import RawIdentifierModel

class WordModel():
    name: str = None
    lineNumbers: [int] = None
    separatedWords = None

    def __init__(self, raw_identifier_model: RawIdentifierModel):
        self.init_data(raw_identifier_model)
        self.separate_identifier()
        self.split_word_at_underscores()

    def init_data(self, raw_identifier_model: RawIdentifierModel):
        self.name = raw_identifier_model.get_name()
        self.lineNumbers = [raw_identifier_model.get_line()]
        self.separatedWords = []

    def to_print(self):
        return {
            "line_numbers": self.lineNumbers,
            "separated_words": self.separatedWords
        }

    def append_line_number(self, line_number: int):
        self.lineNumbers.append(line_number)
    
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
        self.separatedWords = separated_word

    def insert_underscore(self, separated_word, index):
        return separated_word[:index] + "_" + separated_word[index:]

    def insert_underscore_before(self, separated_word, index):
        return separated_word[:index - 1] + "_" + separated_word[index - 1:]

    def split_word_at_underscores(self):
        self.separatedWords = [word for word in self.separatedWords.lower().split("_") if len(word) > 0]