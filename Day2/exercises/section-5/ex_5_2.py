import subprocess

def capture_command_output(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

output = capture_command_output(["ls", "-l"])
print(output)
