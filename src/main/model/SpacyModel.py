import spacy

class SpacyModel():
    spacy_nlp = None

    def __init__(self):
        self.spacy_nlp = spacy.load("en", disable=["parser", "tagger", "ner", "textcat"])

    def get_spacy_nlp(self):
        return self.spacy_nlp