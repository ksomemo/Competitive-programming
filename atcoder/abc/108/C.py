def main():
    """
    1 <= N, K <= 2 * 10^5

    a,b,c (ok: a=b=c)

    """
    N, K = map(int, input().split())
    ans = f(N, K)
    # ans = TLE(N, K)
    print(ans)


def f(N, K):
    ans = 0
    return ans


def TLE(N, K):
    ans = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                if (a + b) % K == 0 and \
                    (b + c) % K == 0 and \
                        (c + a) % K == 0:
                    ans += 1
    return ans


if __name__ == '__main__':
    main()
