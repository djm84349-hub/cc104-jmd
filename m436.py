def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        return 28
    if month in (4, 6, 9, 11):
        return 30
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    return "Invalid month"


def day_of_year(year, month, day):
    days_before_month = 0
    for current_month in range(1, month):
        days_before_month += days_in_month(year, current_month)
    return days_before_month + day


print(day_of_year(2000, 12, 31))
