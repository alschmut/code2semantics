from gensim.models import Word2Vec
from util.Logger import Logger
from util.Timer import Timer

class Word2VecModel():

    model: Word2Vec = None
    class_name: str = None
    file_context_name: str = None

    def exists(self):
        return self.model != None

    def set_model(self, model_file_path: str):
        timer: Timer = Timer()
        Logger().start_analyzing("Loading Word2VecModel")
        self.model = Word2Vec.load(model_file_path)
        Logger().finish_analyzing(timer.get_duration(), "Loading Word2VecModel")

    def set_class_name(self, class_identifier_words: []):
        self.class_name = self.get_most_similar(class_identifier_words)[0]

    def set_file_context_name(self, file_context_words: []):
        self.file_context_name = self.get_most_similar(file_context_words)[0]

    def get_model(self):
        return self.model

    def is_word_in_dictionary(self, word: str):
        return word != None and self.model.wv.vocab.get(word) != None

    def get_vector(self, word: str):
        return self.model.wv[word]

    def get_distance(self, word1, word2):
        if self.is_word_in_dictionary(word1) and self.is_word_in_dictionary(word2):
            return self.model.wv.distance(word1, word2)

    def get_most_similar(self, word_list):
        filtered_word_list = [word for word in word_list if self.is_word_in_dictionary(word)]
        if filtered_word_list:
            return self.model.wv.most_similar(positive=filtered_word_list, topn=1)[0]

    def get_distance_to_class(self, word):
        return self.get_distance(word, self.class_name)

    def get_distance_to_file_context(self, word):
        return self.get_distance(word, self.file_context_name)

instance: Word2VecModel = Word2VecModel()