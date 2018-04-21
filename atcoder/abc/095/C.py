def main():
    """
    1 <= A,B,C<=5*10^3
    1 <= X,Y<=10^5
    """
    A, B, C, X, Y = map(int, input().split())

    # A,B片方をを愚直に用意
    # A,BをABから愚直に用意
    a4 = A * X + min(B * Y, 2 * C * Y)
    a5 = B * Y + min(A * X, 2 * C * X)
    a6 = 2 * C * max(X, Y)

    a1 = 2 * C * min(X, Y)
    d = abs(X - Y)
    price = A if X >= Y else B
    a1 += min(price * d, 2 * C * d)

    # ABからAを作る
    a2 = float("inf")
    if 2 * C < A:
        d = max(Y - X, 0)
        a2 = 2 * C * X + min(B * d, 2 * C * d)

    # ABからBを作る
    a3 = float("inf")
    if 2 * C < B:
        d = max(X - Y, 0)
        a3 = 2 * C * Y + min(A * d, 2 * C * d)

    ans = min([a1, a2, a3, a4, a5, a6])
    print(ans)


if __name__ == '__main__':
    main()
