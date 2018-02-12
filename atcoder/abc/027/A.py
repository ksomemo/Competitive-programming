def main():
    L = map(int, input().split())

    d = {}
    for l in L:
        d[l] = d.get(l, 0) + 1

    for l, c in d.items():
        if c % 2 == 1:
            print(l)


if __name__ == '__main__':
    main()
