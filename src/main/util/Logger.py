import time

class Logger():

    RAW_WIKI_LINES: int = 4672758
    processed_articles = None

    def __init__(self):
        self.processed_articles = 0

    def info(self, message: str):
        print(f"INFO : {message}")

    def debug(self, message: str):
        print(f"DEBUG: {message}")

    def warn(self, message: str):
        print(f"WARN : {message}")

    def error(self, message: str):
        print(f"ERROR: {message}")

    def start_analyzing(self, message: str):
        print(f"\r... Analyzing: {message}", end="")

    def finish_analyzing(self, seconds: float, message: str):
        print(f"\rINFO : Finished ({seconds}s): {message}")
            
    def every_n_wiki_status(self, n: int, duration: float = 0):
        self.processed_articles = self.processed_articles + 1
        if (self.processed_articles % n == 0):
            self.wiki_status(duration)

    def wiki_status(self, duration: float = 0):
        percent = round(100 / self.RAW_WIKI_LINES * self.processed_articles, 3)
        minutes_left = 0
        if duration > 0 and percent > 0:
            seconds_left = duration / percent * 100
            minutes_left = int(round(seconds_left / 60, 0))
        self.start_analyzing(f"{percent}% (minutes left {minutes_left}) saved {self.processed_articles} articles")

    def usage(self, message: str):
        self.info(f"Usage: {message}")

    def finish_script(self, seconds: float, script_name: str):
        self.info(f"Finished {script_name} in {seconds}s")
