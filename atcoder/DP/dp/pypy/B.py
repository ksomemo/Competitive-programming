def main():
    N, K = map(int, input().split())
    *h, = map(int, input().split())

    ans = f(N, K, h)
    print(ans)


def f(N, K, h):
    dp = [None] * (N + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, N + 1):
        hi = i - 1
        cost = float("inf")
        for k in range(1, K + 1):
            if i - k < 1:
                continue

            tmp = dp[i-k] + abs(h[hi] - h[hi-k])
            cost = min(cost, tmp)

        dp[i] = cost

    ans = dp[N]
    return ans


if __name__ == "__main__":
    main()
