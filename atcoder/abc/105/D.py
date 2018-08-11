def main():
    """
    1 <= N  <= 10^5
    2 <= M  <= 10^9
    1 <= Ai <= 10^9
    1 <= i  <= N

    1 <= l <= r  <= N
    A_l + A_l+1 + ... + Ar = x * M
    """
    N, M = map(int, input().split())
    *A, = map(int, input().split())

    ans = f(N, M, A)
    print(ans)


def f(N, M, A):
    """
    直感: 累積和, 10^5^2: TLE
        二分探索?
    """
    b = [0] * N
    b[0] = A[0]
    for i in range(1, N):
        b[i] = b[i-1] + A[i]

    ans = TLE(N, M, A, b)
    return ans


def TLE(N, M, A, b):
    ans = 0
    for l in range(N):
        for r in range(l, N):
            if l - 1 < 0:
                s = b[r]
            else:
                s = b[r] - b[l-1]
            if s % M == 0:
                ans += 1

    return ans


if __name__ == '__main__':
    main()
