
class ExperienceModel():
	min: int = None
	max: int = None

	def __init__(self, experience_in_years):
		self.min = experience_in_years.get("min")
		self.max = experience_in_years.get("max")


	def to_print(self):
		return {
			"min": self.min,
			"max": self.max
		}