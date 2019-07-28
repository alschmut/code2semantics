import sys, os, spacy
from util.Timer import Timer
from util.FileOpener import FileOpener
from util.Logger import Logger
from model.StopWordModel import StopWordModel

def lemmatize_text(file_path: str):
	logger = Logger()
	nlp = spacy.load("en")
	output_file = FileOpener().get_new_file("wiki.en.lemmatized.txt", "a")
	processed_articles = 0
	with open(file_path, "r") as file:
		for line in file:
			spacy_line = nlp(line)
			lemmatized_list = [word.lemma_ for word in spacy_line]
			lemmazized_line = " ".join(lemmatized_list)
			output_file.write(lemmazized_line)
			processed_articles = processed_articles + 1
			logger.log_every_n_wiki_status(processed_articles, 10)
	logger.log_wiki_status(processed_articles)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <wiki.en.filtered.txt>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Use raw text "{file_path}"')
		print("[+] Starting to lemmatize text")
		timer = Timer()
		lemmatize_text(file_path)
		print(f"\n[+] Finished: {timer.get_duration()}s")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()



