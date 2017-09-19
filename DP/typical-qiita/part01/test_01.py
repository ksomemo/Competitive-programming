def test_sum_max():
    """
    最大和問題
    """
    assert 16 == sum_max([7, -6, 9])
    assert 0 == sum_max([-9, -16])


def sum_max(a):
    N = len(a)
    dp = [0] * (N + 1)

    for i, _a in enumerate(a, 1):
        dp[i] = max(dp[i - 1],
                    dp[i - 1] + _a)

    return dp[-1]
