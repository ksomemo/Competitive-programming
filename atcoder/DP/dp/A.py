def main():
    N = int(input())
    *h, = map(int, input().split())

    ans = f(N, h)
    print(ans)


def f(N, h):
    """
    前から確定させる？
    後から確定させる？
    と考えたけど、

    まずは愚直にやる座標ベース
    1: from (1)       to (2 or 3)
    2: from (1 2)     to (3 or 4)
    3: from (1   3)   to (4 or 5)
    3: from (1 2 3)   to (4 or 5)
    4: from (1 2 3 4) to (5 or 6)
    4: from (1 2   4) to (5 or 6)
    4: from (1   3 4) to (5 or 6)

    コストは絶対値なのであとに行くほど増える
    前から確定させて、コストの少ない進み方をベースにする
    厳密に言えば進み方ではなく、各位置におけるコストだけわかっていれば良い
    """
    dp = [None] * (N + 1)
    dp[0] = 0
    dp[1] = 0
    dp[2] = abs(h[1] - h[0])

    for i in range(3, N + 1):
        hi = i - 1
        cost1 = dp[i-1] + abs(h[hi] - h[hi-1])
        cost2 = dp[i-2] + abs(h[hi] - h[hi-2])
        dp[i] = min(cost1, cost2)

    ans = dp[N]
    return ans


if __name__ == "__main__":
    main()
