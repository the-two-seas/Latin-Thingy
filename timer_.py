# holds timer mechanics in a class
import time
class Timer:
    """timer mechanics"""
    def __init__(self, *, dp: int = 2):
        self.dp = dp
    def start(self):
        self.startCount = time.perf_counter()
    def stop(self):
        self.stopCount = time.perf_counter()
        self.value = round(self.stopCount - self.startCount, self.dp)

