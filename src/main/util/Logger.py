import time

class Logger():

    RAW_WIKI_LINES: int = 4672758

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
        print(f"\rINFO Finished ({seconds}s): {message}")
            
    def every_n_wiki_status(self, num_articles: int, n: int, duration: float = 0):
        if (num_articles % n == 0):
            self.wiki_status(num_articles, duration)

    def wiki_status(self, num_articles: int, duration: float = 0):
        percent = round(100 / self.RAW_WIKI_LINES * num_articles, 3)
        minutes_left = 0
        if duration > 0 and percent > 0:
            seconds_left = duration / percent * 100
            minutes_left = int(round(seconds_left / 60, 0))
        self.start_analyzing(f"{percent}% (minutes left {minutes_left}) saved {num_articles} articles")

    def usage(self, message: str):
        self.info(f"Usage: {message}")

    def finish_script(self, seconds: float, script_name: str):
        self.info(f"Finished {script_name} in {seconds}s")
