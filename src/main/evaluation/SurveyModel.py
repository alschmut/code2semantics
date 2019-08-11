from evaluation.DataSetModel import DataSetModel
from resources import survey

class SurveyModel():
	data_sets: [] = None

	def __init__(self):
		self.data_sets = []
		for data_set in survey.instance:
			self.data_sets.append(DataSetModel(data_set))

	def to_print(self):
		return [data_set.to_print() for data_set in self.data_sets]