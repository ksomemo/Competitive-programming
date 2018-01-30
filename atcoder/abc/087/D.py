def main():
    N, M = map(int, input().split())
    lrd = [
        tuple(map(int, input().split()))
        for _ in range(M)
    ]

    TLE(N, M, lrd)


def TLE(N, M, lrd):
    """
    N,M:10^6より N^2->NG
    矛盾する情報を見つける
    距離情報の保持

    1-2:1, 2-3:1, 1-3:2 <-OK
    1-2:1, 2-3:1, 1-3:5 <-NG(over)
    1-2:1, 2-3:1, 1-3:1 <-NG(less)
    1-2:1, 2-4:3, 1-3:3 <-OK(2-3:2, 3-4:1)
    1-2:1, 2-4:3, 1-3:5 <-NG

    (Li,Ri,Di)
    人Ri は人Li よりも距離 Di だけ右にいる
    すなわち、xRi − xLi = Di
    Ri > Li のとき(人7の右に人8がいる)処理上問題なし
    Ri < Li のとき(人8の右に人7がいる)場合、
    xLi - xRi = -Di
    """
    pass

if __name__ == '__main__':
    main()
