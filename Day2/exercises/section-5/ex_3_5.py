import calendar
from datetime import datetime

def get_weekday_name():
    today = datetime.now()
    return calendar.day_name[today.weekday()]

weekday_name = get_weekday_name()
print(weekday_name)  # Output: Name of the current weekday
