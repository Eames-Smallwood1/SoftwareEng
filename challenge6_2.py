import sys
import datetime

class TimeLogger:
    def isotime(self):
        return datetime.datetime.now().isoformat()

    def event(self, s):
        print(f"{self.isotime()}: {s}")

    def warning(self, s):
        print(f"{self.isotime()}: WARNING: {s}")

class Logger:
    def event(self, s):
        print(s)

    def warning(self, s):
        print(s, file=sys.stderr)

class Divider:
    def __init__(self, l):
        self.logger = l

    def divide(self, a, b):
        if b == 0:
            self.logger.warning("division by zero")
            return None
        self.logger.event(f"dividing {a} by {b}")

        return a / b

t = TimeLogger()
l = Logger()
dl = Divider(l)
dt = Divider(t)

dl.divide(1,2)
dl.divide(10,5)
dl.divide(99,0)
dt.divide(1,2)
dt.divide(10,5)
dt.divide(99,0)