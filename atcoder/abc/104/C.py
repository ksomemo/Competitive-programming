def main():
    """
    1 <=  D <= 100
    1 <= pi <= 100
    1 <=  i <= D
    100 <= G
    100 <= ci <= 10^6

    all: sum(p)
        max: 100 * 10 = 1000
    """
    D, G = map(int, input().split())
    P, C = zip(*(
        map(int, input().split())
        for _ in range(D)
    ))

    # ans = f(D, G, P, C)
    ans = editorial(D, G, P, C)
    print(ans)


def editorial(D, G, P, C):
    """
    bit全探索
        を使う問題
            https://beta.atcoder.jp/contests/abc080/tasks/abc080_c

        https://twitter.com/furuya1223/status/1026100709060562950
        https://twitter.com/furuya1223/status/1026101338675982336
            コンプする点数を決め打ちで2^D全探索(bitで)。
            必ず「0種以上コンプ+未コンプ中最高点のものを0~”その点の問題数-1”問」
            という形になる

            Cは、コンプする場合とそうでない場合で価値が入れ替わりうるので、
            「コンプするものたち」と「コンプしないものたち」で分けて考えたくなった。
            「コンプするもの」は、するかしないかの2値なので、D<=10ということもあり、
            決め打ち全探索ができる
        https://twitter.com/TangentDay/status/1026100759295811584
            C：コンプする集合決め打ちして残りは貪欲

    典型
        https://twitter.com/drken1215/status/1026114800978296832
            今回の C 問題は「bit 全探索」ばかりに目が行きがちだけど、
            それと同じくらい「ある量を決め打つと、残りの最適戦略は Greedy に決まる」
            という超典型の考え方も重要かなと思うん。その意味では

            ABC 085 D - Katana Thrower
            https://beta.atcoder.jp/contests/abc085/tasks/abc085_d

    https://twitter.com/evima0/status/1026100718535499782
        C: 2つの点数を中途半端に埋めても無意味なので1つ除きAll or Nothing (難しめ)

    DP/ナップザック
        https://twitter.com/_TTJR_/status/1026100838681329665
            C: 100 で割ると現実的な時間で DP できるので嬉しいです
        https://twitter.com/kzyKT_M/status/1026101633283813376
            C dp[解いた問題数]=得点
        https://beta.atcoder.jp/contests/abc104/submissions/2958357
        https://beta.atcoder.jp/contests/abc104/submissions/2953341
    その他
        https://twitter.com/satanic0258/status/1026103918353235968
            Cも普通に全探索で,使う個数も降順に1個ずつループしたのでDPなし
    """

    ans = float("inf")
    for i in range(2 ** D):
        c = 0
        score = 0
        clear = [False] * D
        for j in range(D):
            if i & (1 << j):
                c += P[j]
                score += 100 * (j + 1) * P[j] + C[j]
                clear[j] = True

        # print(i, clear, c, score)
        for j in range(D)[::-1]:
            if score >= G:
                break
            if clear[j]:
                continue

            rest = G - score
            base_score = 100 * (j + 1)
            add_c = (rest + base_score - 1) // base_score
            add_c = min(add_c, P[j] - 1)
            c += add_c
            score += base_score * add_c

            # print("\t", base_score, c, score)

        if score >= G:
            ans = min(ans, c)

    return ans


def func_dp(D, G, P, C):
    ans = float("inf")
    return ans


def f(D, G, P, C):
    """
    i, P から問題をすべて分割
    すべての解き方を列挙する
    sum_p ! = 1000 ! => TLE

    点数の高いものから解けばいいとは限らない

    dpっぽく前の解き方を利用してみる
    ans[0] = 0
    ans[1] = max_i * 100 or ボーナスあり
        ボーナスがあるので、前の答え＋点の良い問題とは限らない
        前の解き方のうち、１つ変えるとどうなるか？
            ボーナスがなくなってしまうかもしれない
            代わりにボーナスになる可能性もある
            前の解き方からｘ問変えるとどうなるか？
                同様
    ボーナスもらえるテーブルを作る？
        それとボーナス加味しないDPテーブルとの比較
        b_dp[5] = p1 全完了
        dp[2] = p2
            fix[]
    """
    from itertools import permutations
    from collections import defaultdict

    sum_p = sum(P)
    dp = [float("inf") for _ in range(sum_p + 1)]
    dp[0] = 0
    max_state = {}

    # 総スコアと効率、
    total = [(i + 1) * 100 * P[i] + C[i] for i in range(D)]
    ratio = [total[i] / P[i] for i in range(D)]
    bonus = [False for _ in range(D)]
    for i in range(1, sum_p + 1):
        score = 0
        rest = i
        for j in range(D):
            if bonus[j]:
                rest -= P[j]
                score += total[j]
            elif P[j] <= rest:
                bonus[j] = True
                rest -= P[j]
                score += total[j]

        if dp[i] >= G:
            return i


if __name__ == '__main__':
    main()
