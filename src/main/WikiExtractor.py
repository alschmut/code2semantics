from gensim.corpora import WikiCorpus
import sys, os

from util.Timer import Timer

def get_output_file(file_path: str):
	file_name = file_path.split("/")[-1]
	language_code = file_name[:2]
	output_file_name = f"wiki.{language_code}.text"
	return open(output_file_name, 'w')

def print_status(num_articles: int):
	print(f"\r... Saved {str(num_articles)} articles", end="")

def get_corpus(file_path: str):
	output_file = get_output_file(file_path)
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
		print(f'[-] Usage: python {sys.argv[0]} <<LANG>wiki-latest-pages-articles.xml.bz2>')
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