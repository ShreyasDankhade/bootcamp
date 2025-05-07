metrics = {"requests": 0, "errors": 0}

def increment_requests():
    metrics["requests"] += 1

def increment_errors():
    metrics["errors"] += 1

increment_requests()
increment_errors()
print(metrics)