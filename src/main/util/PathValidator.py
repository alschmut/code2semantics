import os
from util.Logger import Logger

class PathValidator():

    def is_valid_files(self, file_paths: [str], silent: bool = False):
        all_files_valid: bool = True
        for path in file_paths:
            if not os.path.isfile(path):
                all_files_valid = False
                if not silent:
                    Logger().error(f"Could not find file: '{path}'")
        return all_files_valid

    def is_valid_directories(self, dir_paths: [str], silent: bool = False):
        all_directories_valid: bool = True
        for path in dir_paths:
            if not os.path.isdir(path):
                all_directories_valid = False
                if not silent: 
                    Logger().error(f"Could not find directory: '{path}'")
        return all_directories_valid

    def is_valid_paths(self, paths: [str]):
        all_paths_valid = True
        for path in paths:
            if not os.path.exists(path):
                all_paths_valid = False
        return all_paths_valid