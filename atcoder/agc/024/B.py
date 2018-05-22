def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    #f1(N, P)
    editorial(N, P)


def dp(N, P):
    """
    https://beta.atcoder.jp/contests/agc024/submissions/2539848
    https://beta.atcoder.jp/contests/agc024/submissions/2534307
    """
    pass


def uf(N, P):
    """
    https://beta.atcoder.jp/contests/agc024/submissions/2534783
    """
    pass


def editorial(N, P):
    """
    入力例3
        N=8
        P=63127485
         |6   7 8 |
         | 3   4 5|
         |  12    |
        上記の3つの列は要素ai+1=aiである部分列
            連続する列が長いほど、移動しなくて済む要素は多い
            連続するためには、最小未満は左・最大より大きいものは末尾に移動する
        部分列
            残った要素がもとの数列における相対的な序列を保つ
            与えられた列からいくつかの要素を取り去ることによって得られる列
    """
    if N == 1:
        print(0)
        return

    # WA(N, P)
    a = [0] * (N+1)
    for i, p in enumerate(P):
        a[p] = i

    tmp = 1
    max_len = 1
    for i in range(1, N):
        if a[i] < a[i+1]:
            tmp += 1
            max_len = max(max_len, tmp)
        else:
            tmp = 1

    ans = N - max_len
    print(ans)


def WA(N, P):
    tmp = 0
    ans = 0
    for i, p in enumerate(P):
        if i == 0 or P[i-1] + 1 == p:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1

    print(N - ans)


def reference():
    """
    Aを手前に動かすと
    A以下全部動かさないといけないことが分かるので
    最長増加列を動かさなければ良いことが分かる
        https://twitter.com/eiya5498513/status/998205587438497792

    一つ数字を決めて
    それ以下を左にそれ以上を右に揃えるのにかかる手数を考える set使った、nlogn
        https://twitter.com/hewla/status/998204793989419009

    dpでもできるらしい
        https://twitter.com/tempura_pp/status/998206453583302657
        https://twitter.com/yfba_/status/998204228043620352

    UnionFindでもできるらしい
        https://twitter.com/keidaroo/status/998204595603046401
    """
    pass


def f(N, P):
    """
    入力例1
      1324
     213 4   34soretd
    12 3 4
    ------
    その他
      1324
      1 243   12sorted
      1 2 34

    末尾より大きいものを後ろに
        5234
         2345 
    ただし末尾を先頭に移動することでsortされるかも
        5674
       4567

    逆順sortされている場合
        54321  4以降を順に先頭へ移動
    部分的にsortされている箇所をどうする？

    231456  1以外sort済み
    145623  23以外sort済み

    min,maxのindexをもつ
    [3, 2, 5, 1, 4, 6]
              3     5
    """
    pass


def f1(N, P):
    idx_min, idx_max = 0, 0
    s = [False] * N
    for i, p in enumerate(P):
        if p == 1:
            idx_min = i
        elif p == N:
            idx_max = i

        # 部分的にsortされているか
        if i == 0 or P[i-1] < p:
            s[i] = True
    _min, _max = P[idx_min], P[idx_max]

    print(P)
    print(s)
    print(idx_min, idx_max)


if __name__ == '__main__':
    main()
