def main():
    """
    4 <= N <= 2 * 10^5
    1 <= Ai <= 10^9
    """
    N = int(input())
    *A, = map(int, input().split())

    ans = f(N, A)
    ans = TLE(N, A)

    print(ans)


def f(N, A):
    ans = 0

    return ans


def TLE(N, A):
    ans = float("inf")
    for b in range(1, N-2):
        for c in range(b+1, N-1):
            for d in range(c+1, N):
                B = A[:b]
                C = A[b:c]
                D = A[c:d]
                E = A[d:]
                print(B, C, D, E)

                *sums, = map(sum, [B, C, D, E])
                x = abs(max(sums) - min(sums))
                ans = min(ans, x)

    return ans


if __name__ == '__main__':
    main()
