def main():
    """
    input:
        1 <= H <= 100
        1 <= W <= 8
        1 <= K <= W

    output:
        数列の項の最大公約数の最大値
    """
    H, W, K = map(int, input().split())

    ans = f(H, W, K)
    print(ans)


def f(H, W, K):
    """
    1-2の間に横棒を引く
    引き方: 0-H に引く組合せ
        x = sum(nCr(H, i) for i in range(H+1))

    2-3の間に横棒を引く
    引き方: 1-2の引いた部分以外に引くことができる
        startが1からなのでたどり方的に上に引く必要がないが
        それも正しい可能性のあるあみだくじなので考慮する

        x = 0
        for i in range(H+1):
            # i 本引いてあるなら、引いてない部分がMAX
            for j in range(H-i+1):
                x += sum(nCr(j, k) for k in range(j))

    たどり方
    1の一番高い棒から2へ向かう or なければそのまま下へ
    2から1or3の棒へ向かう or なければ下へ

    Kにたどり着くパターン or (全パターン - たどりつけないパターン)
        たぶん、縦と横を独立に考える。なんとなく
        下にH
        横にK-1, 右を+1左を-1としたとき
    """
    mod = 10 ** 9 + 7
    ans = 0

    return ans % mod


if __name__ == '__main__':
    main()
