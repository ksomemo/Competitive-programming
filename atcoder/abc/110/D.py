def main():
    """
    1 <= N <= 10^5
    1 <= M <= 10^9

    正整数 N, M
    a1 * a2 * ... * aN = M となる長さNの数列a
    何通りあるか
    数列A1-ai != 数列A2-ai
    """
    N, M = map(int, input().split())

    ans = f(N, M)
    print(ans)


def factorize(N):
    """素因数分解

    TODO: もっと速い方法
    素因数がある場合は範囲をsqrtで狭められるが、ない場合愚直に探してしまう
    N以下の素数を見つけて、それだけで対応すれば速いはず
    """
    import math
    factors = []
    while True:
        if N % 2 == 0:
            factors.append(2)
            N //= 2
        else:
            break
    m = int(math.sqrt(N))
    i = 3
    while i <= m:
        add = False
        while True:
            if N % i == 0:
                factors.append(i)
                N //= i
                add = True
            else:
                break
        if add:
            m = int(math.sqrt(N))
        i += 2
    if N > 1:
        factors.append(N)
    return factors


def f(N, M):
    """
    M を素因数分解すると約数とそれらの個数がわかる
    それらの組合せを制約を満たすようにする
    1 * M, M * 1 をわすれないこと:
        1 * 1 * 1 * M もOK

    3 12
        1,1,12: 3P3 / 2!
        2,2,3:  3P3 / 2!
        3,4,1:  3P3
        6,2,1:  3P3

    http://sucrose.hatenablog.com/entry/2014/10/10/235805
    """
    ans = 0
    m = 10 ** 9 + 7
    factors = factorize(M)
    from collections import Counter
    c = Counter(factors)
    print(c)
    return ans


if __name__ == '__main__':
    main()
