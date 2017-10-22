def main():
    N = int(input())
    X = [int(x) for x in input().split()]

    # solve1(N, X)
    solve2(N, X)


def solve1(N, X):
    # 10^5 ^ 2 = 10^10, TLEしそう
    ans = float("inf")
    for i, x1 in enumerate(X):
        for x2 in X[i + 1:]:
            ans = min(ans, abs(x1 - x2))

    if ans == float("inf"):
        print(0)
    else:
        print(ans)


def solve2(N, X):
    # sortしてから引けばよさそう
    ans = float("inf")
    for i, x1 in enumerate(X[-1:], 1):
        x2 = X[i]
        if x1 == x2:
            continue
        ans = min(ans, abs(x1 - x2))

    if ans == float("inf"):
        print(0)
    else:
        print(ans)


if __name__ == '__main__':
    main()
