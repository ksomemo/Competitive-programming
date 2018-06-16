def main():
    """
    1 <= N <= 1000
    0 <= M <= N
    - 10^10 <= xi,yi,zi <= 10^10
    """
    N, M = map(int, input().split())
    xyz = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ans = f(N, M, xyz)
    print(ans)


def f(N, M, xyz):
    """
    N種類のケーキを売っている
    各種類のケーキには「綺麗さ」「おいしさ」「人気度」の 3つの値を持ち, 
    i種類目のケーキ
        綺麗さ: xi
        おいしさ: yi
        人気度: zi

    M個のケーキを食べることにした.
    彼は次のように, 食べるケーキの組み合わせを選ぶことにした.

    同じ種類のケーキを 2個以上食べない.
    (綺麗さの合計の絶対値) + (おいしさの合計の絶対値) + (人気度の合計の絶対値) 
        が最大になるように選ぶ.

    iを食べる食べない0/1の全通り
        2^(10^3) => TLE

    たべてないとき: 0
    スコア値ans:
        max(ans, たべるときのスコア)
        たべるときのスコア:
            今までの合計が分からないと計算できない
            保持する必要がある

        現在、AとCでスコア最大であるとき
            Dを食べるとする
            そのとき食べなかったBを考慮に入れるべきか？
                絶対値が下がるのでいれなくてよい？
                きれいは上がるが、おいしさは下がるなどありそう

            abs(A+C+B) + abs(A+C+B) + abs(A+C+B)
            abs(A+C)   + abs(A+C)   + abs(A+C)
            abs(A+C+D) + abs(A+C+D) + abs(A+C+D)
    """
    ans = 0
    if N == M:
        sx, sy, sz = 0, 0, 0
        for x, y, z in xyz:
            sx += x
            sy += y
            sz += z

        ans = abs(sx) + abs(sy) + abs(sz)

    return ans


def f2(N, M, xyz):
    """
    N種類の中からM個食べるか食べないかを選択したときの値
    """
    dp = [
        [-float("inf")] * (M+1)
        for _ in range(N)
    ]
    for i in range(N):
        dp[i][0] = 0


if __name__ == '__main__':
    main()
