from datetime import datetime

def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

parsed_date = parse_date("2024-01-01")
print(parsed_date)  # Output: 2024-01-01 00:00:00
