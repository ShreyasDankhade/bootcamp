import subprocess
import time

def run_and_terminate():
    process = subprocess.Popen(["sleep", "10"])  # Simulate a long-running process
    time.sleep(3)  # Let the process run for a few seconds
    process.terminate()  # Terminate the process after 3 seconds
    return process.returncode

return_code = run_and_terminate()
print(return_code)