from datetime import datetime

def format_date():
    return datetime.now().strftime("%Y-%m-%d")

formatted_date = format_date()
print(formatted_date)  # Output: today's date in YYYY-MM-DD format
