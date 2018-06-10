def main():
    """
    1 <= N <= 500
    3 <= C <= 30
    (i!=j): 1 <= D(i,j) <= 1000
    (i==j): 0  = D(i,j)
    1 <= c(i,j) <= C
    """
    N = int(input())
    N, C = map(int, input().split())
    D = [
        list(map(int, input().split()))
        for _ in range(C)
    ]
    c = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    f(N, C, c, D)


def f(N, C, c, D):
    """
    """
    pass


if __name__ == '__main__':
    main()
