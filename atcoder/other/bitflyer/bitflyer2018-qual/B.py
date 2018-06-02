def main():
    A, B, N = map(int, input().split())
    X = input()

    S, C = A, B
    for x in X:
        if x == "S":
            S = max(S-1, 0)
        elif x == "C":
            C = max(C-1, 0)
        elif S >= C and S > 0:
            S -= 1
        elif C > S and C > 0:
            C -= 1

    print(S)
    print(C)


if __name__ == '__main__':
    main()
