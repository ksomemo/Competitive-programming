def main():
    N, M = map(int, input().split())
    *A, = map(int, input().split())
    *B, = map(int, input().split())

    ans = f(N, M, A, B)
    print(ans)


def f(N, M, A, B):
    """
    1 ≤ N  ≤ 1000
    1 ≤ M  ≤ 1000
    1 ≤ Ai ≤ N×M <= 10^6
    1 ≤ Bj ≤ N×M <= 10^6

    書き方
        1マス目: N*M   通り
        2マス目: N*M-1 通り
        (N*M)! 通り: TLE

    A * B による組合せ:
        クロスしたマスそれぞれ行列の最大値が異なるなら、小さい方以下を書く
        クロスしたマスそれぞれ行列の最大値が同じならそこに書くしかない
            よって、他の行列にその値がある場合は書けない
        両方考慮しないと書けるか分からない
        A * B: TLE
    """
    ans = 0
    MOD = 10 ** 9 + 7

    return ans


if __name__ == '__main__':
    main()
