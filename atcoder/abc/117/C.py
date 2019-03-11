def main():
    N, M = map(int, input().split())
    *X, = map(int, input().split())

    ans = f(N, M, X)
    print(ans)


def f(N, M, X):
    """
    1 <= N, M <= 10^5
    |Xi| <= 10^5
    Xi != Xj

    入力例1より初期位置をマスにしてもいいので、0
    N < M なら1回以上動くコマが存在する
    N=1 なら
        X をsortして最小値から最大値まで動かす
    M=N+1 なら
        1動かす
        最後のXに1番近いコマを動かす
        1番近いかを調べるには、X同士の比較なのでN^2: TLE
        外側から内側に移動したほうがよい
            内側から外側に行ってから再度内側に行く場合、損する
            好きな整数座標なので-10^5-1でもよい
        Xをsortしたときの前との差分をとると、どこの間隔が長いか分かる
            その中で短い部分を移動
    """
    if N >= M:
        return 0

    X = sorted(X)
    diff = [abs(X[i+1] - X[i]) for i in range(M-1)]

    # 長い部分は除外する
    ans = sum(sorted(diff, reverse=True)[N-1:])

    return ans


if __name__ == '__main__':
    main()
