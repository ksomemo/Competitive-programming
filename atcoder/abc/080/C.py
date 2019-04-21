def main():
    N = int(input())
    F = [
        [int(x) for x in input().split()]
        for _ in range(N)
    ]
    P = [
        [int(x) for x in input().split()]
        for _ in range(N)
    ]

    ans = f(N, F, P)
    print(ans)


def f(N, F, P):
    """
    N=100=10^2
    曜日*AMPM=10
        Fの組合せ=2^10≒1000=10^3
    10^3*10^2=10^5
    """
    ans = -float("inf")
    for x in range(1, 2 ** 10):
        tmp = 0
        for i in range(N):
            c = 0
            for j in range(10):
                # bit onと店営業中の確認
                if x & (2 ** j) and F[i][j]:
                    c += 1
            tmp += P[i][c]

        ans = max(ans, tmp)

    return ans


if __name__ == '__main__':
    main()
