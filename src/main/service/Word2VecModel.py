from gensim.models import Word2Vec
from util.Logger import Logger
from util.Timer import Timer

class Word2VecModel():

    model: Word2Vec = None

    def set_model(self, model_file_path: str):
        timer: Timer = Timer()
        Logger().start_analyzing("Loading Word2VecModel")
        self.model = Word2Vec.load(model_file_path)
        Logger().finish_analyzing(timer.get_duration(), "Loading Word2VecModel")

    def get_model(self):
        return self.model

    def is_word_in_dictionary(self, word: str):
        return self.model.wv.vocab.get(word) != None

instance: Word2VecModel = Word2VecModel()