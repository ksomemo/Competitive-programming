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

    ans = editorial(N, M, xyz)
    print(ans)


def editorial(N, M, xyz):
    """
    1: max  sum(x)  +  sum(y)  +  sum(z)  (解説用)
    2: max |sum(x)| + |sum(y)| + |sum(z)| (本題)

    1 の場合:
        各ケーキについてスコアを算出し
        スコアが大きいM個を選ぶだけ

    2 の場合:
        |x| = max(x, -x)

          max(|x|, |y|)
        = max(max(x, -x), max(y, -y))
        = max(max(x, y), max(-x, -y))

        3要素について、「正の方向に最大化する」 「負の方向に最大化する」 のどちらを選ぶか、
        ということを考えると分かりやすいです。
        要素は 3 つあるので、2^3 = 8通り全探索します。

        1要素なら分かる
            なにもせずそのままで足す
            符号を反転してからで足す
                ※M個でなく、すべて足すなら反転してもしなくても同じ
        2要素以上
            1の場合(1要素ではなく)を想定しないと場合分けの想定できない
            それぞれの最大化の組合せ

    youtubeのコメントで同じく思ったこと
        1.
            符号を反転してしまって、
            関係ない値が出てきそうに感じちゃうんですけど、
            どうして出ないんでしょうか。
        2.
            元のケーキの符号はそれぞれ決まっていて
            それを足し合わせて符号を決めるのと同義である理由が知りたいです。

    https://twitter.com/_TTJR_/status/1007982375546994688
    """
    max_scores = []
    for i in range(8):
        sign_x = 1 if (1 << 2) & i else -1
        sign_y = 1 if (1 << 1) & i else -1
        sign_z = 1 if (1 << 0) & i else -1

        scores = []
        for x, y, z in xyz:
            s = sum([x * sign_x, y * sign_y, z * sign_z])
            scores.append(s)

        max_s = sum(sorted(scores, reverse=True)[:M])
        max_scores.append(max_s)

    ans = max(max_scores)
    return ans


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

    https://twitter.com/eiya5498513/status/1007993044711297024
    ただDPするだけでは評価基準がないので無理
    """
    dp = [
        [-float("inf")] * (M+1)
        for _ in range(N)
    ]
    for i in range(N):
        dp[i][0] = 0


if __name__ == '__main__':
    main()
