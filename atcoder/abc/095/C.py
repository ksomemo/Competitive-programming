def main():
    """
    1 <= A,B,C<=5*10^3
    1 <= X,Y<=10^5
    """
    A, B, C, X, Y = map(int, input().split())

    search(A, B, C, X, Y)

def search(A, B, C, X, Y):
    """最後の全探索だけでよいらしい
    """
    ans = float("inf")
    for a in range(X+1):
        ab = 2 * (X - a)
        b = max(Y - ab // 2, 0)
        price = A * a + B * b + C * ab
        ans = min(ans, price)

    for b in range(Y+1):
        ab = 2 * (Y - b)
        a = max(X - ab // 2, 0)
        price = A * a + B * b + C * ab
        ans = min(ans, price)

    for ab in range(0, max(X, Y) * 2 + 1, 2):
        a = max(X - ab // 2, 0)
        b = max(Y - ab // 2, 0)
        price = A * a + B * b + C * ab
        ans = min(ans, price)

    print(ans)

def AC(A, B, C, X, Y):
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
