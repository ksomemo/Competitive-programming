import sys
import math


def main():
    """
    2 <= K <= N <= 10^5
    1 <= ai <= N
    1 <= i <= N
    """
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    ans = f_K(N, K, A)
    #ans = editorial(N, K, A)
    print(ans)


def test_examples():
    nka_ans = [
        (4, 3, [2, 3, 1, 4], 2),
        (3, 3, [1, 2, 3], 1),
        (8, 3, [7, 3, 1, 8, 4, 6, 2, 5], 4),
    ]

    for N, K, A, ans in nka_ans:
        assert editorial(N, K, A) == ans
        assert f_K(N, K, A) == ans


def test_ans():
    nka_ans = [
        (5, 2, [1, 2, 3, 4, 5], 4),
        (5, 3, [1, 2, 3, 4, 5], 2),
        (5, 2, [5, 4, 3, 2, 1], 4),
        (5, 3, [5, 4, 3, 2, 1], 2),
    ]

    for N, K, A, ans in nka_ans:
        assert editorial(N, K, A) == ans
        assert f_K(N, K, A) == ans


def f_K(N, K, A):
    """
    最初に置く範囲は、 1_idx - K + 1 から 1_idx
    """
    idx = [i for i, a in enumerate(A) if a == 1][0]
    left_idx = max(0, idx - K)
    ans = float("inf")
    for i in range(left_idx, idx + 1):
        left = i
        right = max(0, N - left - K)
        tmp = (left + (K - 1) - 1) // (K - 1)
        tmp += 1
        tmp += (right + (K - 1) - 1) // (K - 1)
        ans = min(ans, tmp)

    return ans


def editorial(N, K, A):
    """
    端から端までカバーしていく
        K + (K - 1) * N (N >= 0)
        これは仮に１番左に1があったとき
    結果的には順番は気にしなくて良い
    上記でカバーしていくと、いつかは最初の1をカバーする
        カバーした順番を1をカバーしたことを最初に行えば変わらない

    TODO: editorial pdfの意味
        1 + g(K − 1) ≤ p ≤ 1 + (g + 1)(K − 1) なる整数 g
    """
    return ((N-1) + (K-1) - 1) // (K-1)


def WA(N, K, A):
    """
    数列のうち，連続した K個の要素を選ぶ
    その後，選んだ要素それぞれの値を，選んだ要素の中の最小値で置き換える．
    上の操作を何回か繰り返すことで，この数列の要素をすべて等しくしたい
    必要な操作の回数の最小値


    全体の最小値=1のindexを見つける, 1-idx
        1でない最小値で統一したとき
        最終的に統一できない
            N=3,K=2, 231
            23 to 22: 221

    1-idxを含むKを左右に置き換えていく
        N=3,K=2, 213
        21 to 11: 113
        13 to 11: 111

    Kの範囲がはみだすときは調整
        N=5,K=3, 51234
        513 to 111
    """
    idx = 0
    for i, a in enumerate(A):
        if a == 1:
            idx = i
            break

    ans = 0
    if idx - K + 1 < 0:
        print("A", file=sys.stderr)
        # 左の範囲調整
        idx = K - 1
        ans += 1
        if idx <= N - 2:
            # 残り右
            rest = N - (idx + 1)
            print(idx, rest, file=sys.stderr)
            ans += math.ceil(rest / (K - 1))
    elif idx + K - 1 >= N:
        print("B", file=sys.stderr)
        # 右の範囲調整
        idx = N - K
        ans += 1
        if idx >= 1:
            # 残り左
            rest = idx
            print(idx, rest, file=sys.stderr)
            ans += math.ceil(rest / (K - 1))
    else:
        print("C", file=sys.stderr)
        # 右
        rest = N - (idx + 1)
        ans += math.ceil(rest / (K - 1))
        # 左
        rest = idx
        ans += math.ceil(rest / (K - 1))

    return ans


if __name__ == '__main__':
    main()
