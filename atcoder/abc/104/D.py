def main():
    """
    1 <= i < j < k <= |T|
    Ti = A
    Tj = B
    Tk = C
    """
    S = input()
    ans = editorial(S)
    ans2 = dp_simple(S)
    ans3 = cumsum(S)

    assert ans == ans2 == ans3
    if len(S) <= 5:
        ans4 = TLE(S)
        assert ans == ans4

    print(ans)


def TLE(S):
    """文字列全列挙
    ?をすべて置き換えるパターンを作成し
    それについてABC数を算出
    """
    s = list(S)
    qi = [i for i, c in enumerate(S) if c == "?"]
    nq = len(qi)
    mod = 10 ** 9 + 7
    import sys
    sys.setrecursionlimit(mod)

    def rec(i):
        if i == nq:
            return n_ABC(s)

        ans = 0
        for x in list("ABC"):
            s[qi[i]] = x
            ans += rec(i+1)

        return ans

    ans = rec(0) % mod
    return ans


def n_ABC(S):
    """3^Q を考えていないパターン がABCを求めるパターンになっていた
    """
    ans = 0
    n = len(S)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # print(i, j, k, S[i] + S[j] + S[k])
                if S[i] in ("A", "?") and S[j] in ("B", "?") and S[k] in ("C", "?"):
                    ans += 1

    return ans


def editorial(S):
    MOD = 10 ** 9 + 7
    n = len(S)
    dp = [[0] * (3+1) for _ in range(n+1)]

    for i in range(n, -1, -1):
        for j in range(3, -1, -1):
            if i == n:
                x = int(j == 3)
                # ≠3: 丸を3個つける前に最後の文字まで見終わってしまい、手遅れ
                # =3: 処理が正常終了
                dp[i][j] = x
            else:
                m1 = 1
                if S[i] == "?":
                    m1 = 3

                if j == 3:
                    # 丸は3個つけ終わったので、あとは?を置換するのみ
                    dp[i][j] = m1 * dp[i+1][j]
                else:
                    m2 = int(S[i] == "?" or S[i] == "ABC"[j])
                    # 前半:i文字目に丸をつけない場合, 後半:丸をつける場合に対応
                    dp[i][j] = m1 * dp[i+1][j] + m2 * dp[i+1][j+1]

                dp[i][j] %= MOD

    ans = dp[0][0]
    return ans


def dp_simple(S):
    n = len(S)
    MOD = 10 ** 9 + 7
    dp = [[0] * (3+1) for _ in range(n+1)]
    # 組合せ列挙なので掛け算としての単位元
    dp[0][0] = 1

    for i in range(n):
        # i文字目まで
        for j in range(3+1):
            # 0-3文字揃ってる
            m = 1
            if S[i] == "?":
                # 置換できるので3パターン
                m = 3
            dp[i+1][j] += dp[i][j] * m
            dp[i+1][j] %= MOD

            # 3文字揃ってないとき, 対応する文字になるか？
            if j < 3 and (S[i] == "?" or S[i] == "ABC"[j]):
                dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] %= MOD

    ans = dp[n][3]
    return ans


def cumsum(S):
    """
    考えたときに累積和が浮かんだ
    ABCとあるので
    i文字目までのA相当の数、つまり?も含んだ数
    これをBとCにも適用する
    Aを決め打ちで進めるとBも走査することになる
    Cは定数倍で求められるが、|S|^2: TLE で意味がない

    ここで断念していろいろ調べると
    Bを決め打ちすれば
    A: 0-(B-1)
    C: (B+1)-N
    なのでNでおｋ

    と、思ったがWAと同じ間違いをしている
    3^q パターンをきちんと考える
    """
    n = len(S)
    aa = [0 for _ in range(n+1)]
    cc = [0 for _ in range(n+1)]
    q = [0 for _ in range(n+1)]
    for i in range(n):
        aa[i+1] += aa[i] + int(S[i] == "A")
        cc[i+1] += cc[i] + int(S[i] == "C")
        q[i+1] += q[i] + int(S[i] == "?")

    ans = 0
    MOD = 10 ** 9 + 7
    for i in range(1, n-1):
        a = aa[i]
        c = cc[n] - cc[i+1]
        l = q[i]
        r = q[n] - q[i+1]
        # ABC の作り方
        # AB?: ? 1つをCに割り当てる
        # ?BC: ? 1つをAに割り当てる
        # ?B?: ? 2つをACに割り当てる
        if S[i] in ("B", "?"):
            ac = a * c * pow(3, l + r, MOD)
            aq, qc, qq = (0, 0, 0)
            if l + r - 1 >= 0:
                p = pow(3, l + r - 1, MOD)
                aq = a * r * p
                qc = l * c * p
            if l + r - 2 >= 0:
                qq = l * r * pow(3, l + r - 2, MOD)
            # print(a, c, l, r, ((l+r, l+r-1, l+r-2)), (ac, aq, qc, qq))
            # 3^x: xが負になるときに少数になってしまうので、float -> int にする必要がある
            # 上記が重いのでTLE: pow+mod引数で対応
            ans += ac + aq + qc + qq
            ans %= MOD

    return ans


def twi(S):
    """
    DP
        https://twitter.com/furuya1223/status/1026100709060562950
            DPのD。Aの場合と?にAを入れる場合を特別扱いすることに注意
        https://twitter.com/evima0/status/1026100718535499782
            左から?をA,B,Cに変えつつ3文字に丸をつけて左から読むとABCになるようにDP (難しめ) 
        https://twitter.com/TangentDay/status/1026100759295811584
            D：dp[i文字目][ABCどこまで進んだか]
        https://twitter.com/_TTJR_/status/1026100838681329665
            D: i 文字目までで "A", "AB", "ABC" がそれぞれいくつ作れるか dp する
            (普通にソコソコの難易度)
            https://twitter.com/_TTJR_/status/1026101862880227328
                というか D は DP じゃなくてもできる気がしてきた 
                (全ての B について、その左に A がいくつあるかと、
                その右に C がいくつあるかが分かれば良いので)
        https://twitter.com/yfba_/status/1026102627606487042
            DP[i][j][k] := i文字目までで,
            ?でA, B, Cにするときj=1, 2, 3,
            ?じゃないときj=0, "ABC"のk文字目まで揃ってる場合の数。
            https://twitter.com/yfba_/status/1026104049194520576
                Dはひたすら3次元DP配列を切って書いてた。
    典型への落とし込み
        https://twitter.com/osrehun/status/1026101499103916032
            Dは3つ要素あるときは真ん中に注目するという典型だなと思いました。
        https://twitter.com/tempura_pp/status/1026106474945105920
            そりゃ数え上げ得意と自称してるから
            B固定して両端考えて各組み合わせに応じて3の何とか乗を足せばいいみたいなのすぐ気づくけど
            ABConlyにはさすがにキツくないか
        B固定めっちゃ賢いな。言われてみれば常套手段か 

        →ただし、DPのほうが楽らしいが
        https://twitter.com/eiya5498513/status/1026105413345767424
        https://twitter.com/eiya5498513/status/1026106165288099841
            DのDP解はDPであることに気が付くのが一番難しくて、
            出れば漸化式は「取るor取らない」
            という典型的なものに?による*3がくっついただけなので難しくないです。

        B固定つまり真ん中固定と典型
            https://twitter.com/noss46/status/1026101536693186561
            https://twitter.com/noss46/status/1026109780144734208
                D 累積和してB固定で考えると…
                (昨日: mujin-2018)
                昨日のCの曲がる地点もそうだし今日のDのB固定も
                どこを固定したら楽になるかみたいなところが共通してますね
    その他
        https://twitter.com/rian_tkb/status/1026101284686848000
            D は真ん中のB (or ?) を決めて左右を下記の4つを足した
                A, C を使う
                A, ? を使う
                ?, C を使う
                ?, ? を使う
        https://twitter.com/kzyKT_M/status/1026101633283813376
            D Bの位置を決めて、右のA?と左のC?を数えて、3^?を掛け合わせたりする

    連レス
        https://twitter.com/satanic0258/status/1026100804493565952
            数学？累積和とB固定の詳細？
            DPにしてスッキリ版
                https://twitter.com/satanic0258/status/1026105434971680768
                https://beta.atcoder.jp/contests/abc104/submissions/2959673
        https://twitter.com/furuya1223/status/1026102311846727683
            DP詳細
    """
    ans = 0
    return ans


if __name__ == '__main__':
    main()
