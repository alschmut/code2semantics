import sys, os, json
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.FileName import FileName
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

def calculate_semantic_distance(model_file_path: str, project_file_path: str):
	model: Word2Vec = Word2Vec.load(model_file_path)
	project: ProjectModel = json.loads(FileOpener().get_file_content(project_file_path))
	output_file = FileOpener().get_new_file("wiki.en.semantic_distance.csv")
	output_file.writelines("path,semantic_distance\n")

	for file in project:
		word_list: [str] = get_word_list(model, file)
		avg_distance = get_avg_distance(model, word_list)
		output_file.writelines(file.get("name") + "," + str(avg_distance) + "\n")

def main():
	script_name: str = FileName().get_file_name_from_path(sys.argv[0])

	if len(sys.argv) != 3:
		Logger().usage(f"python {script_name} <word2vec.model> <project_data.json>")
		return

	model_file_path = sys.argv[1]
	project_file_path = sys.argv[2]

	if os.path.isfile(model_file_path) and os.path.isfile(project_file_path):
		Logger().info(f'Use model "{model_file_path}"')
		Logger().info(f'Use project_data "{project_file_path}"')
		Logger().info("Starting to calculate semantic distance")
		timer = Timer()
		calculate_semantic_distance(model_file_path, project_file_path)
		Logger().finish_script(timer.get_duration(), script_name)
	else:
		Logger().error(f"Could not find file: {model_file_path} or {project_file_path}")

if __name__ == '__main__':
    main()