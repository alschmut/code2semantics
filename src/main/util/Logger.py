import time

class Logger():

    RAW_WIKI_LINES: int = 4672758

    def log_every_n_wiki_status(self, num_articles: int, n: int, duration: float = 0):
        if (num_articles % n == 0):
            self.log_wiki_status(num_articles, duration)

    def log_wiki_status(self, num_articles: int, duration: float = 0):
        percent = round(100 / self.RAW_WIKI_LINES * num_articles, 3)
        minutes_left = 0
        if duration > 0 and percent > 0:
            seconds_left = duration / percent * 100
            minutes_left = int(round(seconds_left / 60, 0))
        print(f"\r... {percent}% (minutes left {minutes_left}) saved {num_articles} articles", end="")
