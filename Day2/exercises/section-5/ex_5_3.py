import subprocess

def check_exit_code(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        return f"Command failed with exit code {result.returncode}"
    return "Command executed successfully"

status = check_exit_code(["ls", "-l"])
print(status)
