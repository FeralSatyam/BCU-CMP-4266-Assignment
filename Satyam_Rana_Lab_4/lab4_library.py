def is_leap(year):
    if year % 400 == 0:
        print("Leap Year")
    else:
        if year % 100 == 0:
            print("Not leap year")
        else:
            if year % 4 == 0:
                print("Leap year")

def get_days_of_month(month: int, year: int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    else:
        return -1