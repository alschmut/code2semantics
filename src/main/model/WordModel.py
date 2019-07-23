class WordModel():
    name: str = None
    lineNumbers: int = None
    partial = None

    def __init__(self, identifier):
        self.name = identifier.get("name")
        self.lineNumbers = [identifier.get("line")]
        self.partial = []

    def get_separated_word_obj(self):
        self.separate_identifier()
        self.split_word_at_underscores()
        return {
            "lineNumbers": self.lineNumbers,
            "partial": self.partial
        }
    
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
        self.partial = separated_word

    def insert_underscore(self, separated_word, index):
        return separated_word[:index] + "_" + separated_word[index:]

    def insert_underscore_before(self, separated_word, index):
        return separated_word[:index - 1] + "_" + separated_word[index - 1:]

    def split_word_at_underscores(self):
        self.partial = [word for word in self.partial.lower().split("_") if len(word) > 0]