from evaluation.ExperienceModel import ExperienceModel

class ParticipantModel():
    work_path: str = None
    experience: ExperienceModel = None
    clean_code_practitioner: str = None

    def __init__(self, participant_data):
        self.work_path = participant_data.get("work_path")
        self.experience = ExperienceModel(participant_data.get("experience_in_years"))
        self.clean_code_practitioner = participant_data.get("clean_code_practitioner")

    def to_print(self):
        return {
            "work_path": self.work_path,
            "experience": self.experience.to_print(),
            "clean_code_practitioner": self.clean_code_practitioner
        }