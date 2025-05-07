import psutil

def print_resource_usage():
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    print(f"Memory usage: {memory.percent}%")
    print(f"CPU usage: {cpu}%")

print_resource_usage()
