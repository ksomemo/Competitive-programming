def main():
    """
    N=2*10^5
    """
    N = int(input())
    A = map(int, input().split())
    B = map(int, input().split())

    TLE(N, A, B)


def f(N, A, B):
    pass


def TLE(N, A, B):
    A = list(A)
    B = list(B)

    ans = 0
    for a in A:
        for b in B:
            ans ^= a + b

    print(ans)


if __name__ == '__main__':
    main()
