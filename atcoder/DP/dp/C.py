def main():
    N = int(input())
    abc = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ans = f(N, abc)
    print(ans)


def f(N, abc):
    """
    2回連続で同じ活動(abc)を行えない

    1: a or b or c
    2:
        1-a: b or c
        1-b: c or a
        1-c: a or b

    1日目
        aをしたときの幸福最大
        bをしたときの幸福最大
        cをしたときの幸福最大
    2日目
        aをしたときの幸福最大(b, c から)
        bをしたときの幸福最大(c, a から)
        cをしたときの幸福最大(a, b から)
    """
    dp = [[None] * 3 for _ in range(N + 1)]
    dp[0] = [0, 0, 0]
    dp[1] = abc[0]

    for i in range(2, N + 1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + abc[i-1][0]
        dp[i][1] = max(dp[i-1][2], dp[i-1][0]) + abc[i-1][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + abc[i-1][2]

    ans = max(dp[N])
    return ans


if __name__ == "__main__":
    main()
