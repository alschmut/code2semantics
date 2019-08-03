from evaluation.FileModel import FileModel
from evaluation.ParticipantModel import ParticipantModel

class DataSetModel():
	participant = None
	files: dict = None

	def __init__(self, participant_data, files):
		self.participant = ParticipantModel(participant_data)
		self.files = {}
		for file in files:
			file_name = list(file.get("class_names").keys())[0]
			self.files[file_name] = FileModel(file)


	def to_print(self):
		return {
			"participant": self.participant.to_print(),
			"files": {key: value.to_print() for (key, value) in self.files.items()}
		}