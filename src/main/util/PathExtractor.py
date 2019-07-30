import os

class PathExtractor():

    def get_absolute_path(self, path: str):
        return os.path.abspath(path)

    def get_file_name(self, path: str):
        absolute_path = self.get_absolute_path(path)
        return absolute_path.split("/")[-1]