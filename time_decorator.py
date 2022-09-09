import time


def my_decorator(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        stop = time.time()
        ms = stop - start
        print(f"{f.__name__} takes {ms * 1000} ms to execute")
        return result

    return wrapper
