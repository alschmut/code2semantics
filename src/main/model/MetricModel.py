from model.MetricType import MetricType

class MetricModel():

    type: MetricType = None
    value: float = None

    def __init__(self, type: MetricType, value: int):
        self.type = type
        self.value = value

    def to_print(self):
        return {
            "type": self.type.value,
            "value": self.value
        }
    
    def get_value(self):
        return self.value

    def increment_value_by_1(self):
        self.value = self.value + 1
