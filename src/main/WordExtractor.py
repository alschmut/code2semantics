class WordExtractor(object):
    def extract_multi_words(self, identifier):
        new_identifier = {}
        for identifier_type in identifier.keys():
            new_identifier[identifier_type] = []
            for multi_word in identifier.get(identifier_type):
                separated_word = WordExtractor.get_separated_word(self, multi_word)
                separated_word_object = WordExtractor.get_separated_word_object(self, multi_word, separated_word)
                new_identifier[identifier_type].append(separated_word_object)
        return new_identifier

    def get_separated_word(self, multi_word):
        last_char = multi_word[0]
        index = 1
        while index < len(multi_word):
            current_char = multi_word[index]
            if last_char.islower() and current_char.isupper():
                multi_word = WordExtractor.insert_underscore(self, multi_word, index)
                index += 1

            if last_char.isupper() and current_char.islower():
                multi_word = WordExtractor.insert_underscore_before(self, multi_word, index)
                index += 1

            index += 1
            last_char = current_char
        return multi_word

    def insert_underscore(self, separated_word, index):
        return separated_word[:index] + "_" + separated_word[index:]

    def insert_underscore_before(self, separated_word, index):
        return separated_word[:index - 1] + "_" + separated_word[index - 1:]

    def get_separated_word_object(self, multi_word, separated_word):
        return {
            "name": multi_word,
            "partial": [word for word in separated_word.lower().split("_") if len(word) > 0]
        }