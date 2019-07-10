import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import sys, os, time

def get_output_file(file_path):
	file_name = file_path.split("/")[-1]
	language_code = file_name.split(".")[1]
	output_file_name = f"wiki.{language_code}.semantic_distance.csv"
	return open(output_file_name, 'wb')

def calculate_semantic_distance(file_path, parser_path):
	model = Word2Vec.load(file_path)
	word_list = []
	model.most_similar(positive=word_list, topn=1)

def get_time_duration(start):
	end = time.time()
	return round(end - start, 2)

def main():
	if len(sys.argv) != 3:
		print(f'[-] Usage: python {sys.argv[0]} <word2vec.model> <parser_data.json>')
		return

	model_file_path = sys.argv[1]
	parser_file_path = sys.argv[2]

	if os.path.isfile(model_file_path) and os.path.isfile(parser_file_path):
		print(f'[+] Use model "{model_file_path}"')
		print(f'[+] Use parser_data "{parser_file_path}"')
		print("[+] Starting to calculate semantic distance")
		start = time.time()
		calculate_semantic_distance(model_file_path, parser_file_path)
		print(f"[+] Finished: {get_time_duration(start)} seconds")
	else:
		print(f"[-] Could not find file: {parser_file_path}")

if __name__ == '__main__':
    main()