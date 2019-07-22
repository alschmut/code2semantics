import multiprocessing
import sys, os
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from util.Timer import Timer

def get_output_model(file_path: str):
	file_name = file_path.split("/")[-1]
	language_code = file_name.split(".")[1]
	output_file_name = f"wiki.{language_code}.word2vec.model"
	return open(output_file_name, 'wb')

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
	model.save(get_output_model(file_path))

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <wiki.<LANG>.text>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Use corpus "{file_path}"')
		print("[+] Starting to train word2vec model")
		timer = Timer()
		train_model(file_path)
		print(f"[+] Finished: {timer.get_duration()} seconds")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()