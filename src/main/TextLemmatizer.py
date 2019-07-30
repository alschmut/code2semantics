import sys, os, spacy
from util.Timer import Timer
from util.FileOpener import FileOpener
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from model.SpacyModel import SpacyModel

def lemmatize_text(file_path: str, timer: Timer):
	logger = Logger()
	output_file = FileOpener().get_new_file("wiki.en.lemmatized.txt", "a")
	processed_articles = 0
	
	with open(file_path, "r") as file:
		for line in file:
			lemmatized_list = [word.lemma_ for word in SpacyModel().get_en_spacy_line(line) if not word.is_stop]
			lemmazized_line = " ".join(lemmatized_list)
			output_file.write(lemmazized_line)
			processed_articles = processed_articles + 1
			logger.every_n_wiki_status(processed_articles, 10, timer.get_duration())
	logger.wiki_status(processed_articles)

def main():
	script_name: str = PathExtractor().get_file_name(sys.argv[0])

	if len(sys.argv) != 2:
		Logger().usage(f"python {script_name} <wiki.en.filtered.txt>")
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		Logger().info(f'Use raw text "{file_path}"')
		Logger().info("Starting to lemmatize text")
		timer = Timer()
		lemmatize_text(file_path, timer)
		Logger().finish_script(timer.get_duration(), script_name)
	else:
		Logger().error(f"Could not find file: {file_path}")

if __name__ == '__main__':
    main()



