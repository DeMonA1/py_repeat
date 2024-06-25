import time
from timeit import timeit


def snooze():
    time.sleep(1)

seconds = timeit('snooze()', globals=globals(), number=1)
print('%.4f' % seconds)

def time_decorator(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"{(t2-t1):.4f}")
        return result
    return inner

@time_decorator
def naptime():
    snooze()

naptime()


class TimeContextManager:
    
    def __enter__(self):
        self.t1 = time.time()
        return self
    
    def __exit__(self, type, value, traceback):
        t2 = time.time()
        print(f"{(t2-self.t1):.4f}")
        
with TimeContextManager():
    snooze()