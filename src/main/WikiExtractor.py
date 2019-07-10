from gensim.corpora import WikiCorpus
import sys, os, time

def get_output_file(file_path):
	file_name = file_path.split("/")[-1]
	language_code = file_name[:2]
	output_file_name = f"wiki.{language_code}.text"
	return open(output_file_name, 'w')

def print_status(num_articles):
	print(f"\r... Saved {str(num_articles)} articles", end="")

def get_corpus(file_path):
	output_file = get_output_file(file_path)
	wiki = WikiCorpus(file_path, lemmatize=False, dictionary={})
	i = 0

	for text in wiki.get_texts():
		output_file.write(" ".join(text) + "\n")
		i = i + 1
		if (i % 100 == 0):
			print_status(i)

	output_file.close()
	print_status(i)

def get_time_duration(start):
	end = time.time()
	return round(end - start, 2)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <<LANG>wiki-latest-pages-articles.xml.bz2>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Use wiki "{file_path}"')
		print("[+] Starting to create wiki corpus")
		start = time.time()
		get_corpus(file_path)
		print(f"[+] Finished: {get_time_duration(start)} seconds")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()