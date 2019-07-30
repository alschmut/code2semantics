import string
from model.RawIdentifierModel import RawIdentifierModel
from nltk.corpus import stopwords

class StopWordModel():
    stop_words: set = None

    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.add_extra_words()

    def add_extra_words(self):
        for char in string.ascii_lowercase:
            self.stop_words.add(char)

    def get_stop_words(self):
        return self.stop_words

instance: StopWordModel = StopWordModel()