import time

class Logger():

    RAW_WIKI_LINES: int = 4672758

    def log_every_n_wiki_status(self, num_articles: int, n: int):
        if (num_articles % n == 0):
            self.log_wiki_status(num_articles)

    def log_wiki_status(self, num_articles: int):
        percent = round(100 / self.RAW_WIKI_LINES * num_articles, 3)
        print(f"\r... Saved {percent}% {str(num_articles)} articles", end="")
