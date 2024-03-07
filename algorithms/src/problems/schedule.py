from collections import defaultdict


month_map = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


day_map = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_week_day(first_day, h_day, h_month, month_days):

    current_day = first_day

    for i in range(1, h_month+1):
        
        # in 28 days there will be the same day, but it will 29 date
        current_day = (current_day + month_days[i-1] - 28) % 7

    return (current_day + h_day - 1) % 7


def find_best_worst_days(year, holidays, first_day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_year = [52] * 7
    days_in_year[first_day] = 53

    if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        days_in_year[(first_day+1) % 7] = 53
        month_days[1] = 29

    for h_day_year, h_month in holidays:
    
        day_of_week = get_week_day(first_day, h_day_year, h_month, month_days)
        
        days_in_year[day_of_week] -= 1

    best = 0
    worst = 1

    for i, days in enumerate(days_in_year):

        if days > days_in_year[best]:
            best = i
    
        elif days < days_in_year[worst]:
            worst = i

    return day_map[best], day_map[worst]


if __name__ == '__main__':
    n = int(input())
    year = int(input())

    holidays = []
    for _ in range(n):
        day, month = input().split()
        holidays.append(
            (int(day), month_map.index(month))
        )
    first_day = day_map.index(input())

    best, worst = find_best_worst_days(year, holidays, first_day)
    print(best + " " + worst)
