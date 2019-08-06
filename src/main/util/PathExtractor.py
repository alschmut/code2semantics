import os

class PathExtractor():

    def get_absolute_path(self, path: str):
        return os.path.abspath(path)

    def get_file_name(self, path: str):
        absolute_path = self.get_absolute_path(path)
        return os.path.basename(absolute_path)

    def get_file_extension(self, file_name: str):
        return file_name.split(".")[-1]

    def get_relative_path(self, path: str):
        basepath: str = os.path.abspath(os.path.curdir)
        return path[len(basepath) + 1:] if path.startswith(basepath) else path