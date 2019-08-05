import sys
from util.Timer import Timer
from util.FileOpener import FileOpener
from util.Logger import Logger
from util.PathExtractor import PathExtractor
from util.PathValidator import PathValidator
from model.SpacyModel import SpacyModel

def lemmatize_text(file_path: str, timer: Timer):
	logger = Logger()
	output_file = FileOpener().get_new_file("wiki.en.lemmatized.txt", "a")
	
	with open(file_path, "r") as file:
		for line in file:
			lemmatized_list = [word.lemma_ for word in SpacyModel().get_en_spacy_line(line)]
			lemmazized_line = " ".join(lemmatized_list)
			output_file.write(lemmazized_line)
			logger.every_n_wiki_status(10, timer.get_duration())
	logger.every_n_wiki_status(1)

def main():
	script_name: str = PathExtractor().get_file_name(sys.argv[0])

	if len(sys.argv) != 2:
		Logger().usage(f"python {script_name} <wiki.en.filtered.txt>")
		return

	file_path = sys.argv[1]

	if PathValidator().is_valid_files([file_path]):
		Logger().info(f'Use raw text "{file_path}"')
		Logger().info("Starting to lemmatize text")
		timer = Timer()
		lemmatize_text(file_path, timer)
		Logger().finish_script(timer.get_duration(), script_name)

if __name__ == '__main__':
    main()



