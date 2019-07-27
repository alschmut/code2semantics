import sys, os
from util.Timer import Timer
from util.FileOpener import FileOpener
from util.Logger import Logger
from model.StopWordModel import StopWordModel

def remove_stopwords(file_path: str):
	logger = Logger()
	stop_words = StopWordModel().get_stop_words()
	output_file = FileOpener().get_new_file("wiki.en.filtered.txt", "a")
	processed_articles = 0
	with open(file_path, "r") as file:
		for line in file:
			split_line = line.split(" ")
			filtered_list = [word for word in split_line if word not in stop_words]
			filtered_line = " ".join(filtered_list)
			output_file.write(filtered_line)
			processed_articles = processed_articles + 1
			logger.log_every_n_wiki_status(processed_articles, 100)
	logger.log_wiki_status(processed_articles)

def main():
	if len(sys.argv) != 2:
		print(f'[-] Usage: python {sys.argv[0]} <wiki.en.raw.txt>')
		return

	file_path = sys.argv[1]

	if os.path.isfile(file_path):
		print(f'[+] Use raw text "{file_path}"')
		print("[+] Starting to remove stopwords")
		timer = Timer()
		remove_stopwords(file_path)
		print(f"\n[+] Finished: {timer.get_duration()}s")
	else:
		print(f"[-] Could not find file: {file_path}")

if __name__ == '__main__':
    main()



