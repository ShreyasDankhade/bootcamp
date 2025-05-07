import multiprocessing
import time

def compute_square(number):
    time.sleep(1)
    return number ** 2

def start_process():
    process = multiprocessing.Process(target=compute_square, args=(5,))
    process.start()
    process.join()  # Wait for the process to finish

start_process()