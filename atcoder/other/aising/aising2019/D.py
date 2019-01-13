def main():
    N, Q = map(int, input().split())
    *A, = map(int, input().split())
    X = [int(input()) for _ in range(Q)]

    ans = f(N, Q, A, X)
    print(ans)


def f(N, Q, A, X):
    """
    """
    ans = 0
    return ans


if __name__ == '__main__':
    main()
