import sys, os
from gensim.corpora import WikiCorpus
from util.FileOpener import FileOpener
from util.Timer import Timer
from util.Logger import Logger
from util.FileName import FileName

def get_corpus(file_path: str):
	logger = Logger()
	output_file = FileOpener().get_new_file("wiki.en.raw.txt")
	wiki: WikiCorpus = WikiCorpus(file_path, lemmatize=False, dictionary={})
	processed_articles = 0

	for text in wiki.get_texts():
		output_file.write(" ".join(text) + "\n")
		processed_articles = processed_articles + 1
		logger.every_n_wiki_status(processed_articles, 100)

	output_file.close()
	logger.wiki_status(processed_articles)

def main():
	script_name: str = FileName().get_file_name(sys.argv[0])

	if len(sys.argv) != 2:
		Logger().usage(f'python {script_name} <en.wiki-latest-pages-articles.xml.bz2>')
		return

	file_path: str = sys.argv[1]

	if os.path.isfile(file_path):
		Logger().info(f'Starting to create wiki corpus from "{file_path}"')
		timer = Timer()
		get_corpus(file_path)
		Logger().finish_script(timer.get_duration(), script_name)
	else:
		Logger().error(f"Could not find file: {file_path}")

if __name__ == '__main__':
    main()