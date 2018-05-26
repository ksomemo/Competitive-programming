def main():
    N = int(input())
    rs = input()

    table = {
        r: i
        for i, r in enumerate("ABCDF"[::-1])
    }
    s = 0
    for r in rs:
        s += table[r]

    ans = s / N
    print("{0:.20f}".format(ans))


if __name__ == '__main__':
    main()
