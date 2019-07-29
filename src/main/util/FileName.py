import os

class FileName():

    def get_absolute_path(self, path: str):
        return os.path.abspath(path)

    def get_file_name_from_path(self, path: str):
        absolute_path = self.get_absolute_path(path)
        return absolute_path.split("/")[-1]