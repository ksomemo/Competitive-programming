def main():
    day = input()

    w = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ]
    if day in w:
        idx = w.index(day)
        print(5 - idx)
    else:
        print(0)


if __name__ == '__main__':
    main()
