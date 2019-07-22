import time

class Timer():

    startTime: float
    stopTime: float

    def __init__(self):
        self.startTime = time.time()

    def get_duration(self):
        self.stopTime = time.time()
        return round(self.stopTime - self.startTime, 2)
