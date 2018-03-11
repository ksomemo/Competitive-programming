def main():
    N, K = map(int, input().split())

    TLE(N, K)


def TLE(N, K):
    """
    1 <= a,b <= N <= 10^5
    a mod b >= K
    0 <= K <= N-1
    """
    # a < b: mod b = a, K <= a <= N
    ans = 0
    for a in range(K, N):
        b_pattern = N - a
        ans += b_pattern

    # a > b: mod b = x
    # K >= b: mod b = 0 or K< より
    # K < b < a <= N
    for a in range(K+2, N+1):
        for b in range(K+1, a):
            if a % b >= K:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
