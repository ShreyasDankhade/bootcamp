from datetime import datetime, timedelta

def add_days_to_today(days):
    return datetime.now() + timedelta(days=days)

new_date = add_days_to_today(7)
print(new_date)  # Output: current date + 7 days
