from datetime import datetime, timedelta

def round_to_nearest_hour():
    now = datetime.now()
    return now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1) if now.minute >= 30 else now.replace(minute=0, second=0, microsecond=0)

rounded_time = round_to_nearest_hour()
print(rounded_time)  # Output: current time rounded to the top of the hour
