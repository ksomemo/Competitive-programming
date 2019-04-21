def main():
    N, M = map(int, input().split())
    ans = editorial(N, M)
    print(ans)


def editorial(N, M):
    """
    1 回の実行にかかる時間を x ms
    全てのケースに正解する確率を p
    この問題の答えを y ms

    x = 1900M + 100(N − M)
    p = (1/2)^M

    まず，一回目の提出で必ず x ms はかかる
    その後は，確率 p で終了
    そして確率 1 − p でその提出には失敗し，更に提出を繰り返す
    確率 1 − p で失敗した場合の，その時点からかかる時間の期待値は y ms
    よって，y = x + (1 − p) × y が成立し
    これを解くと y = x/p が得られる
    答えは x/p = (1900M + 100(N − M)) × 2M
    """
    return (1900 * M + 100 * (N - M)) * (2 ** M)


if __name__ == '__main__':
    main()
