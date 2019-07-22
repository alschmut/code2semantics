import multiprocessing
import sys, os, time, json
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from FileOpener import FileOpener
from model.ProjectModel import ProjectModel

def get_avg_distance(model: str, word_list: [str]):
	most_similar_word_pair = model.wv.most_similar(positive=word_list, topn=1)
	print(most_similar_word_pair)
	centric_word = most_similar_word_pair[0][0]
	distances_to_centric_vector = model.wv.distances(centric_word, word_list)
	distance = 0
	for word_tuple in distances_to_centric_vector:
		distance += word_tuple
	return distance / len(word_list)

def get_word_list(model, file):
	word_list = []
	identifiers = file.get("identifiers")
	for type in identifiers:
		for word_obj in identifiers.get(type):
			filtered_words = [word for word in word_obj.get("partial") if model.wv.vocab.get(word) != None]
			word_list.extend(filtered_words)
	return word_list

def get_output_file(file_path: str):
	file_name = file_path.split("/")[-1]
	language_code = file_name.split(".")[1]
	output_file_name = f"wiki.{language_code}.semantic_distance.csv"
	return open(output_file_name, 'w')

def calculate_semantic_distance(model_file_path: str, project_file_path: str):
	model: Word2Vec = Word2Vec.load(model_file_path)
	project: ProjectModel = json.loads(FileOpener().get_file_content(project_file_path))
	output_file = get_output_file(model_file_path)
	output_file.writelines("path,semantic_distance\n")

	for file in project:
		word_list: [str] = get_word_list(model, file)
		print(file.get("name"))
		avg_distance = get_avg_distance(model, word_list)
		output_file.writelines(file.get("name") + "," + str(avg_distance) + "\n")

def get_time_duration(start: float):
	end: float = time.time()
	return round(end - start, 2)

def main():
	if len(sys.argv) != 3:
		print(f'[-] Usage: python {sys.argv[0]} <word2vec.model> <project_data.json>')
		return

	model_file_path = sys.argv[1]
	project_file_path = sys.argv[2]

	if os.path.isfile(model_file_path) and os.path.isfile(project_file_path):
		print(f'[+] Use model "{model_file_path}"')
		print(f'[+] Use project_data "{project_file_path}"')
		print("[+] Starting to calculate semantic distance")
		start: float = time.time()
		calculate_semantic_distance(model_file_path, project_file_path)
		print(f"[+] Finished: {get_time_duration(start)}s")
	else:
		print(f"[-] Could not find file: {project_file_path}")

if __name__ == '__main__':
    main()