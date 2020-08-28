
def leap_years(n):
    current_years = 0
    start_year = 2021
    while current_years < n:
        if id_leap2(start_year):
            current_years += 1
            print(start_year)
        start_year += 1


def id_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def id_leap2(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


if __name__ == '__main__':
    leap_years(10)