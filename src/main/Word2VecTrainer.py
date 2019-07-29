import multiprocessing
import sys, os
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from util.Timer import Timer
from util.FileOpener import FileOpener
from util.Logger import Logger
from util.FileName import FileName

def trim_unneeded_RAM(model: Word2Vec):
	model.init_sims(replace=True)
	return model

def train_model(file_path: str):
	size = 100
	window = 5
	min_count = 5
	model_type = {"cbow": 0, "skip_gram": 1}

	model = Word2Vec(LineSentence(file_path), sg = model_type["cbow"], 
		size=size, window=window, min_count=min_count, workers=multiprocessing.cpu_count())

	model = trim_unneeded_RAM(model)
	model.save(FileOpener().get_new_file("wiki.en.word2vec.model", "wb"))

def main():
	script_name: str = FileName().get_file_name_from_path(sys.argv[0])

	if len(sys.argv) != 2:
		Logger().info(f'python {script_name} <wiki.en.clean.txt>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		Logger().info(f'Use corpus "{file_path}"')
		Logger().info("Starting to train word2vec model")
		timer = Timer()
		train_model(file_path)
		Logger().finish_script(timer.get_duration(), script_name)
	else:
		Logger().error(f"Could not find file: {file_path}")

if __name__ == '__main__':
    main()