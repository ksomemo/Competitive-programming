def main():
    """
    1 <= i < j < k <= |T|
    Ti = A
    Tj = B
    Tk = C
    """
    S = input()
    ans = editorial(S)

    print(ans)


def f(S):
    """
    """
    pass


def editorial(S):
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
