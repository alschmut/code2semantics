class WordExtractor(object):
    def extract_multi_words(self, parser_data):
        extracted_identifier = {}
        
        for identifier_type in parser_data.get("identifier").keys():
            extracted_identifier[identifier_type] = []
            for multi_word in parser_data.get("identifier").get(identifier_type):
                separated_word = multi_word
                last_character = ""
                index = 0
                while index < len(separated_word):
                    current_last_character = separated_word[index]
                    if last_character.islower() and separated_word[index].isupper():
                        separated_word = separated_word[:index] + "_" + separated_word[index:]
                        index += 1

                    if last_character.isupper() and separated_word[index].islower():
                        separated_word = separated_word[:index - 1] + "_" + separated_word[index - 1:]
                        index += 1

                    index += 1
                    last_character = current_last_character

                extracted_word_object = {
                    "name": multi_word,
                    "partial": [word for word in separated_word.lower().split("_") if len(word) > 0]
                }
                extracted_identifier[identifier_type].append(extracted_word_object)

        parser_data["identifier"] = extracted_identifier
        return parser_data

    def parse_kotlin_file(self, input_stream):
        pass

    def combine_as_map(self, identifier, keywords):
        return {
            "identifier": identifier,
            "keywords": keywords
        }

# groß groß -> nichts
# groß klein -> füge vor dem großen ein
# klein klein -> nichts
# klein groß -> füge zwischen drin ein