import spacy

class SpacyModel():
    spacy_en_nlp = None

    def __init__(self):
        self.spacy_en_nlp = spacy.load("en", disable=["parser", "tagger", "ner", "textcat"])

    def get_en_spacy_line(self, line: str):
        return self.spacy_en_nlp(line)