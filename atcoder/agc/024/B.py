def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    f1(N, P)

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
