def main():
    _ = input()
    a = sorted(int(i) for i in input().split())
    a_len = len(a)
    if a_len % 2 == 0:
        idx = a_len // 2
        median = sum(a[idx - 1:idx + 1]) / 2
        print(round(median, 1))
    else:
        print(a[a_len // 2])


if __name__ == '__main__':
    main()
