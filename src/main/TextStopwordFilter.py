import sys, os
from util.Timer import Timer
from util.FileOpener import FileOpener
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from service.StopWordModel import StopWordModel

def remove_stopwords(file_path: str):
	logger = Logger()
	stop_words = StopWordModel().get_stop_words_nltk()
	output_file = FileOpener().get_new_file("wiki.en.filtered.txt", "a")
	processed_articles = 0
	with open(file_path, "r") as file:
		for line in file:
			split_line = line.split(" ")
			filtered_list = [word for word in split_line if word not in stop_words]
			filtered_line = " ".join(filtered_list)
			output_file.write(filtered_line)
			processed_articles = processed_articles + 1
			logger.every_n_wiki_status(processed_articles, 100)
	logger.wiki_status(processed_articles)

def main():
	script_name: str = PathExtractor().get_file_name(sys.argv[0])

	if len(sys.argv) != 2:
		Logger().usage(f'python {script_name} <wiki.en.raw.txt>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		Logger().info(f'Use raw text "{file_path}"')
		Logger().info("Starting to remove stopwords")
		timer = Timer()
		remove_stopwords(file_path)
		Logger().finish_script(timer.get_duration(), script_name)
	else:
		Logger().error(f"Could not find file: {file_path}")

if __name__ == '__main__':
    main()



