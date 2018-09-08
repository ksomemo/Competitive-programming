def main():
    """
    1 <= N  <= 10^5
    1 <= X  <= 10^9
    1 <= xi <= 10^9
    xi != xj
    xi != X
    """
    N, X = map(int, input().split())
    *xs, = map(int, input().split())

    ans = f(N, X, xs)
    print(ans)


def f(N, X, xs):
    """
    直線上に N 個の都市
    i 番目の都市は座標 xi

    あなたの目的は、これら全ての都市を 1度以上訪れること
    あなたは、はじめに正整数 Dを設定
    その後、あなたは座標 Xから出発し、以下の移動 1、移動 2を好きなだけ行う

        移動 1: 座標 yから座標 y+Dに移動する
        移動 2: 座標 yから座標 y−Dに移動する

    全ての都市を 1 度以上訪れることのできる Dの最大値を求めよ
    ここで、都市を訪れるとは、その都市のある座標に移動すること


    D=1, OK
    """
    ds = [abs(X - x) for x in xs]
    ans = ds[0]
    from fractions import gcd

    for d in ds:
        ans = gcd(d, ans)

    return ans


if __name__ == '__main__':
    main()
