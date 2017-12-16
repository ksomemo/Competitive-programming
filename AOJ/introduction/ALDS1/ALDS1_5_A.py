from itertools import product


def main():
    """
    2^20 = 1,048,576
    q = 200
    200,000,000
    limit 5s より総当りOK
    """
    n = int(input())
    A = list(map(int, input().split()))
    q = int(input())
    M = map(int, input().split())

    dp(n, A, q, M)


def combination(n, A, q, M):
    for m in M:
        if m == 0 or solve(m, A, n):
            print("yes")
        else:
            print("no")


def dp(n, A, q, M):
    M_max = 2000
    _dp = [False] * (M_max + 1)
    for a in A:
        # 小さい順から評価すると、後の評価に影響する(aを2回足すことになる)
        for i in range(M_max, 0, -1):
            if _dp[i] and i + a <= M_max:
                _dp[i + a] = True
        # 先に設定すると、倍数を全て許容するためあとで
        _dp[a] = True

    for m in M:
        if _dp[m]:
            print("yes")
        else:
            print("no")


def solve(m, A, n):
    # for b in f1(n):
    for b in product([0, 1], repeat=n):
        s = sum(a * bit for a, bit in zip(A, b))
        if m == s:
            return True

    return False


def f1(n):
    for i in range(2 ** n):
        # 0/1をn個返すためにbitを利用
        # 0b を削除
        bit = bin(i)[2:]
        yield map(int, bit.zfill(n))

if __name__ == '__main__':
    main()
