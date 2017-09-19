def test_knapsack():
    """
    ナップサック問題
    """
    max_weight = 8
    w_v = [
        (2, 3), (1, 2), (3, 6), (2, 1), (1, 3), (5, 85)
    ]
    res = knapsack(max_weight, w_v)
    assert 91 == res


def knapsack(W, weight_value):
    N = len(weight_value)
    inf = float("inf")
    dp = [
        [-inf] * (W + 1)
        for _ in range(N + 1)
    ]
    for i in range(N + 1):
        dp[i][0] = 0

    for i, (w, v) in enumerate(weight_value):
        for lim_w in range(W + 1):
            # i番目まででのそれぞれの重さ
            if lim_w < w:
                # 追加して超えるならそのまま
                dp[i + 1][lim_w] = dp[i][lim_w]
            else:
                # 追加できるなら、
                # 重さを減らして追加する場合と比較
                dp[i + 1][lim_w] = max(dp[i][lim_w],
                                       dp[i][lim_w - w] + v)

    return dp[N][W]
