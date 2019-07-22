import sys, os, spacy
from util.Timer import Timer
from util.FileOpener import FileOpener

def lemmatize_wiki(file_path: str):
    sp = spacy.load("en")
    output_file = FileOpener().get_new_file("wiki.en.lemmatised.text", "a")
    with open(file_path, "r") as file:
        for line in file:
            spacy_line = sp(line)
            lemmatized_list = [word.lemma_ for word in spacy_line]
            lemmazized_line = " ".join(lemmatized_list)
            output_file.write(lemmazized_line)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <wiki.en.raw.text>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Use raw text "{file_path}"')
		print("[+] Starting to lemmatize text")
		timer = Timer()
		lemmatize_wiki(file_path)
		print(f"[+] Finished: {timer.get_duration()}s")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()



