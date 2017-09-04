def main():
    N = int(input())
    if is_leap_year(N):
        print("Yes")
    else:
        print("No")


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
