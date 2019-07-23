import sys, os
from gensim.corpora import WikiCorpus
from util.FileOpener import FileOpener
from util.Timer import Timer

def print_status(num_articles: int):
	print(f"\r... Saved {str(num_articles)} articles", end="")

def get_corpus(file_path: str):
	output_file = FileOpener().get_new_file("wiki.en.raw.txt")
	wiki: WikiCorpus = WikiCorpus(file_path, lemmatize=False, dictionary={})
	i = 0

	for text in wiki.get_texts():
		output_file.write(" ".join(text) + "\n")
		i = i + 1
		if (i % 100 == 0):
			print_status(i)

	output_file.close()
	print_status(i)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <en.wiki-latest-pages-articles.xml.bz2>')
		return

	file_path: str = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Starting to create wiki corpus from "{file_path}"')
		timer = Timer()
		get_corpus(file_path)
		print(f"[+] Finished: {timer.get_duration()} seconds")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()