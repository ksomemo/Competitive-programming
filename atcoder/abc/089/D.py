def main():
    H, W, D = map(int, input().split())
    A = [
        list(map(int, input().split()))
        for _ in range(H)
    ]
    Q = int(input())
    LR = [
        list(map(int, input().split()))
        for _ in range(Q)
    ]

    f(H, W, D, A, Q, LR)


def f(H, W, D, A, Q, LR):
    """
    距離を計算しておく
    """
    pos = [None for _ in range(H * W + 1)]
    for y in range(H):
        for x in range(W):
            a = A[y][x]
            pos[a] = (x, y)

    d = [0 for _ in range(H * W + 1)]
    for i in range(1, D + 1):
        current = i
        dist = 0
        while current + D <= H * W:
            _next = current + D
            i, j = pos[current]
            x, y = pos[_next]

            dist += abs(x - i) + abs(y - j)

            # print((j, i), "to", (y, x), "cur", current, "next", _next, dist)
            d[_next] = dist
            current = _next

    # print(d)

    for l, r in LR:
        ans = d[r] - d[l]
        print(ans)


def TLE(H, W, D, A, Q, LR):
    """
    Q: 10^5
    H,W: 300
    1 <= D <= H*W = 9 * 10^4
    1 <= L <= R <= H*W
    R-L = n * D
    L=1, R=H*W, D=1: Q * (H*W) = 9 * 10^9 = TLE
    """
    pos = [None for _ in range(H * W + 1)]
    for y in range(H):
        for x in range(W):
            a = A[y][x]
            pos[a] = (x, y)

    for l, r in LR:
        ans = 0
        current = l
        target = r
        while current != target:
            _next = current + D
            i, j = pos[current]
            x, y = pos[_next]

            dist = abs(x - i) + abs(y - j)
            ans += dist

            # print((j, i), "to", (y, x), "cur", current, "next", _next, dist)
            current = _next

        print(ans)


if __name__ == '__main__':
    main()
