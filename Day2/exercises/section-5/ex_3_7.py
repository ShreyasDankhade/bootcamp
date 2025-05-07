import calendar

def generate_month_calendar(year, month):
    return calendar.month(year, month)

month_calendar = generate_month_calendar(2025, 5)
print(month_calendar)
