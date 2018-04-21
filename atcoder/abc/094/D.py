def main():
    """
    nCr の最大化
    2 <= n <= 10^5
        全組合せでは間に合わない
        sortして必要なものを選ぶ
    0 <= ai <= 10^9
        実際に場合の数を求めていては間に合わない
        階乗でO(N)は時間がかかる+数が大きくて処理時間が長い

    nCr = nPr / r!
        nが大きいほど大きい
        rが大きいほど大きい?
    nCr: 7C4 = 7C3
        if r > n // 2
            7C3: 7*6*5 / 3*2
            7C2: 7*6   /   2
        n-r が大きいほど大きい

    ACだったけど解説動画からのメモ
        二項係数
        大きさを比べる時差で無理なら比を取る
    """
    n = int(input())
    *a, = map(int, input().split())

    a = sorted(a)
    m = a[-1]
    m2 = m // 2
    r, r_tmp = 0, 0
    for _a in a:
        tmp = _a
        if _a > m2:
            tmp = m - _a
        
        if tmp > r_tmp:
            r = _a
            r_tmp = tmp

    print(m, r)


if __name__ == '__main__':
    main()
