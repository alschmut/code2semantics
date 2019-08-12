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

    def get_type(self):
        return self.type
    
    def get_value(self):
        return self.value

    def is_absolute(self):
        return self.type is MetricType.Absolute

    def is_relative(self):
        return self.type is MetricType.Relative

    def increment_value_by_1(self):
        self.value += 1
