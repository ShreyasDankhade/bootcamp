from datetime import datetime

def compare_dates(date1, date2):
    return min(date1, date2)

date1 = datetime(2024, 1, 1)
date2 = datetime(2025, 5, 5)
earlier_date = compare_dates(date1, date2)
print(earlier_date)  # Output: 2024-01-01 00:00:00
