def main():
    """
    input:
        1 <= N <= 10^5
        N <= M <= 10^9

        a1 + a2 + ... + aN = M
        1 <= ai

    output:
        数列の項の最大公約数の最大値
    """
    N, M = map(int, input().split())

    ans = f(N, M)


def f(N, M):
    """
    最大公約数1:
        1が含まれる
        互いに素

    最大公約数2:
        すべて2の倍数

    N=M: すべて1
    M=奇数: 最大公約数は奇数
    まず1ずつ配る
        M -= N

    N,M: 0は偶数、1は奇数
    0 0: 配ってもMは偶数のまま
    0 1: 配ってもMは奇数のまま
         1余るので配る時に２回分配る、余りはどれかに割り当てて偶数にする
    1 0: 奇数回目の配るときには奇数、偶数回目のときは偶数
    1 1: 配ってもMは奇数のまま、01と同じパターン

    """
    if N == 1:
        return M

    if N == M or M < N * 2:
        return 1

    # 1回は確実に配れる
    ans = 1
    d = 1
    M -= M
    while M >= N:
        # 配る
        M -= N
        d += 1

        # 残りをいい感じに分配したときに、今まで配った回数の最大公約数を維持できるか?
        if True:
            ans = d

    return ans


def editorial(N, M):
    pass


if __name__ == '__main__':
    main()
