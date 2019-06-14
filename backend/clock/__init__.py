import datetime


class MockClock:
    def __init__(self, current_time):
        self.current_time = datetime.datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")

    def today(self):
        return self.current_time.date()

    def now(self):
        return self.current_time


class RealClock:
    def __init__(self):
        pass

    def today(self):
        return datetime.datetime.now().date()

    def now(self):
        return datetime.datetime.now()