import threading

# Shared variable
counter = 0
counter_lock = threading.Lock()

def increment_counter():
    global counter
    with counter_lock:
        counter += 1
        print(f"Counter: {counter}")

def run_with_lock():
    threads = [threading.Thread(target=increment_counter) for _ in range(5)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

run_with_lock()
