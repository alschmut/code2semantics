from gensim.models import Word2Vec
from util.Logger import Logger
from util.Timer import Timer

class Word2VecModel():

    model: Word2Vec = None

    def exists(self):
        return self.model != None

    def set_model(self, model_file_path: str):
        timer: Timer = Timer()
        Logger().start_analyzing("Loading Word2VecModel")
        self.model = Word2Vec.load(model_file_path)
        Logger().finish_analyzing(timer.get_duration(), "Loading Word2VecModel")

    def get_model(self):
        return self.model

    def is_word_in_dictionary(self, word: str):
        return self.model.wv.vocab.get(word) != None

    def get_vector(self, word: str):
        return self.model.wv[word]

    def get_distance(self, vector1, vector2):
        return self.model.wv.distance(vector1, vector2)

    def get_most_similar_word(self, vector_list):
        filtered_vector_list = [vector for vector in vector_list if self.model.wv.vocab.get(vector) != None]
        if filtered_vector_list:
            return self.model.wv.most_similar(positive=filtered_vector_list, topn=1)[0][0]

instance: Word2VecModel = Word2VecModel()