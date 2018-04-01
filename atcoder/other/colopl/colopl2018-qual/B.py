def main():
    N, X = map(int, input().split())
    S = input()
    T = [int(input()) for _ in range(N)]

    ans = 0
    for c, t in zip(S, T):
        if c == "0":
            ans += t
        else:
            ans += min(X, t)

    print(ans)


if __name__ == '__main__':
    main()
