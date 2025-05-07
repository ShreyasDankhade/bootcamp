import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result

result = run_command(["ls", "-l"])  # Linux/MacOS
# result = run_command(["dir"])  # Windows
print(result.stdout)
