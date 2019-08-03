from evaluation.FileModel import FileModel
from evaluation.ParticipantModel import ParticipantModel

class DataSetModel():
	participant = None
	files: dict = None

	def __init__(self, data_set):
		self.participant = ParticipantModel(data_set.get("participant"))
		self.files = {}
		for (file_name, file) in data_set.get("files").items():
			self.files[file_name] = FileModel(file)


	def to_print(self):
		return {
			"participant": self.participant.to_print(),
			"files": {key: value.to_print() for (key, value) in self.files.items()}
		}