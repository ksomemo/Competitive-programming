def main():
    N = int(input())

    r = {
        (0, 59): "Bad",
        (60, 89): "Good",
        (90, 99): "Great",
        (100, 100): "Perfect"
    }
    for (s, e), x in r.items():
        if s <= N <= e:
            print(x)
            break


if __name__ == '__main__':
    main()
