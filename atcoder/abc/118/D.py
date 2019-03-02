def main():
    N, M = map(int, input().split())
    *A, = map(int, input().split())
    # ans = f(N, M, A)
    ans = editorial(N, M, A)
    print(ans)


def f(N, M, A):
    """
    ちょうど N本のマッチ棒を使って作れる整数の中で最大のものを求めてください。
    ただし、以下の条件を満たさなければなりません。

    作る整数の各桁は、1 から 9 までの数字のうち
        A1,A2,...,AM(1≤Ai≤9) のいずれかでなければならない。
    数字
        1,2,3,4,5,6,7,8,9 を 1つ作るには、それぞれちょうど 
        2,5,5,4,5,6,3,7,6 本のマッチ棒を使う。
    制約
        入力は全て整数である。
        2 ≤ N  ≤ 10^4
        1 ≤ M  ≤ 9
        1 ≤ Ai ≤ 9
        Aiは全て異なる。
        ちょうど N本のマッチ棒を使って条件を満たすように作れる整数が存在する。

    なんとなくDP
    M桁の数字を作る
    条件に合う
    """
    # N本 まで使うか 10^4
    dp = [0] * (N+1)
    cost = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # 桁を追加する→最大のものに桁追加だから、問題なし
    # 桁を入れ替える→無駄、初期状態では0桁しかないので単純に足す
    # どの桁に追加すればよいか？二分探索をして決める。つまり、最大にしたいので逆順ソート済みにする？不要。先頭と末尾に追加で対応

    def digit(x):
        d = 0
        while x % 10 != 0:
            d += 1
            x //= 10
        return d

    for i in range(N+1):
        for a in A:
            # i > 0なら何かしら選んでないといけない
            if i + cost[a] <= N and (i == 0 or dp[i] > 0):
                new_i = i + cost[a]
                # 桁求める、数値のまま。桁まで保持しておけば計算の必要ない？そもそも64ビット越えなのでその対処が必要？
                d = digit(dp[i])
                tmp1 = dp[i] + (10 ** d) * a
                tmp2 = dp[i] * 10 + a
                tmps = [dp[new_i], tmp1, tmp2]
                m = max(tmps)
                dp[new_i] = m
                # print(new_i, tmps, m)

    ans = dp[N]
    return ans


def editorial(N, M, A):
    """
    -inf であれば
        dp[i] = -inf
        dp[new_i] = -inf
            -inf
    0 であれば
        dp[i] = 0
        dp[new_i] = 0
            0
    """
    dp = [-float("inf")] * (N+1)
    # dp = [0] * (N+1)
    dp[0] = 0
    cost = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    # 桁数の決定
    for i in range(N+1):
        for a in A:
            new_i = i + cost[a]
            # if new_i <= N and (i == 0 or dp[i] > 0):
            if new_i <= N:
                m = max(dp[new_i], dp[i] + 1)
                dp[new_i] = m

    ans = 0
    sa = sorted(A, reverse=True)
    n = N
    while n > 0:
        for a in sa:
            nn = n-cost[a]
            # print(n, a, nn, dp[n], dp[nn], sep="\t")
            # dp[nn] == 0 だと、計算できてしまうので不可能な桁数が生まれて無限ループ
            # nn > 0 で、dp[nn] == 0
            if nn >= 0 and dp[n] == dp[nn] + 1:
                ans = ans * 10 + a
                n -= cost[a]
                break

    return ans


if __name__ == "__main__":
    main()
