def main():
    """
    2 <= K < N <= 10^5
    1 <= hi <= 10^9
    """
    N, K = map(int, input().split())
    h = [int(input()) for _ in range(N)]

    ans = f(N, K, h)
    print(ans)


def f(N, K, h):
    h = sorted(h, reverse=True)

    ans = float("inf")
    for i in range(N - K + 1):
        tmp = h[i] - h[i+K-1]
        ans = min(ans, tmp)

    return ans


if __name__ == '__main__':
    main()
