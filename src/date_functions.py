import calendar 
from datetime import date

DEFAULT_FORMAT = "%A, %B %e, %Y"  # e.g. Monday, December 7, 2020

def first_sunday(year, month):
    calendar_month = calendar.monthcalendar(year, month)
    first_sunday = calendar_month[0][6]
    return date(year=year, month=month, day=first_sunday)


def this_year_info():
    year = date.today().year,
    results = {
        "today": date.today(),
        "year": year,
        "first_sundays": []
    }
    for month in range(1, 13): 
        day = first_sunday(year, month)
        results["first_sundays"].append(day)