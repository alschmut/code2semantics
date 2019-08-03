import json
from evaluation.DataSetModel import DataSetModel
from evaluation.resources import file1, file2, file3, participants

class SurveyModel():
	data_sets: [] = None

	def __init__(self):
		self.data_sets = []
		for id in range(16):
			participant_data = [obj for obj in participants.instance if obj.get("ID") == id + 1][0]
			file1_data = self.get_file_from_participant(file1, id)
			file2_data = self.get_file_from_participant(file2, id)
			file3_data = self.get_file_from_participant(file3, id)
			files = [file1_data, file2_data, file3_data]
			self.data_sets.append(DataSetModel(participant_data, files))

	def get_file_from_participant(self, file, id):
		return [obj for obj in file.instance if obj.get("ID") == id + 1][0]

	def to_print(self):
		return [data_set.to_print() for data_set in self.data_sets]