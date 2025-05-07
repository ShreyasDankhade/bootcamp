def check_system_health():
    return {"status": "healthy", "uptime": "48 hours"}

# Example usage
health_status = check_system_health()
print(health_status)