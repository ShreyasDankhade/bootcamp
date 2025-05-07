import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Execution time: {end - start} seconds")

def test_timer():
    with timer():
        time.sleep(2)

test_timer()
