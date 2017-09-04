def main():
    # month == d(1) + d(2)
    days = [
        31, 28, 31, 30,
        31, 30, 31, 31,
        30, 31, 30, 31
    ]
    n_happy_days = 0
    for month, _days in enumerate(days, 1):
        for day in range(1, _days + 1):
            n_happy_days += is_happy_day(month, day)
    print(n_happy_days)


def is_happy_day(month, day):
    if month == (day // 10 + day % 10):
        return True
    else:
        return False

if __name__ == '__main__':
    main()
