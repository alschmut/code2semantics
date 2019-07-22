
class FileOpener():

    def get_file_content(self, file_name: str):
        try:
            with open(file_name, "r") as file:
                return file.read()
        except Exception as err:
            print(f"Could not open file: {type(err)}: {err}")
            return None

    def get_new_file(self, file_path: str, flags: str = "w"):
        return open(file_path, flags)