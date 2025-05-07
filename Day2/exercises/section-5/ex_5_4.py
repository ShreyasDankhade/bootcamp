import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

def start_thread():
    thread = threading.Thread(target=print_numbers)
    thread.start()
    thread.join()  # Wait for the thread to finish

start_thread()
