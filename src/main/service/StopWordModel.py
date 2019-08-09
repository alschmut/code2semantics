import string
from model.IdentifierModel import IdentifierModel
from nltk.corpus import stopwords
from resources import stopwords_smart

class StopWordModel():
    stop_words_nltk: set = None
    stop_words_smart: set = None

    def __init__(self):
        self.stop_words_nltk = set(stopwords.words("english"))
        self.set_stop_words_smart()

    def set_stop_words_smart(self):
        self.stop_words_smart = set()
        for stop_word in stopwords_smart.stop_word_list:
            self.stop_words_smart.add(stop_word)

    def get_stop_words_nltk(self):
        return self.stop_words_nltk

    def get_stop_words_smart(self):
        return self.stop_words_smart

instance: StopWordModel = StopWordModel()