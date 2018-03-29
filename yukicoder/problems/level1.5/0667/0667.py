def main():
    S = input()

    N = len(S)
    ok = S.count("o")
    ng = N - ok
    for i, s in enumerate(S):
        a = ok / (N - i) * 100
        if s == "o":
            ok -= 1
        else:
            ng -= 1
        print(a)


if __name__ == '__main__':
    main()
