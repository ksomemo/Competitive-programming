def main():
    S = input()

    s = "ABCDEF"
    counts = [0] * len(s)
    for i, c in enumerate(s):
        counts[i] = S.count(c)

    print(*counts, sep=" ")


if __name__ == '__main__':
    main()
