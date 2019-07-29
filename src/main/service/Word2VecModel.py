from gensim.models import Word2Vec

class Word2VecModel():

    model: Word2Vec = None

    def set_model(self, model_file_path: str):
        self.model = Word2Vec.load(model_file_path)

    def get_model(self):
        return self.model

    def is_word_in_dictionary(self, word: str):
        return self.model.wv.vocab.get(word) != None

instance: Word2VecModel = Word2VecModel()