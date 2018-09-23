def main():
    """
    1 <= H,W <= 500
    0 <= a(i,j) <= 9
    """
    H, W = map(int, input().split())
    a = [
        list(map(int, input().split()))
        for _ in range(H)
    ]

    # ans = TLE(H, W, a)
    ans = editorial(H, W, a)

    print(len(ans))
    for y1, x1, x, y in ans:
        print(y1+1, x1+1, x+1, y+1)


def editorial(H, W, a):
    op = []
    for i in range(H):
        for j in range(W-1):
            if a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j+1] -= 1
                op.append((i, j, i, j+1))

    for i in range(H-1):
        if a[i][W-1] % 2 == 1:
            a[i][W-1] -= 1
            a[i+1][W-1] -= 1
            op.append((i, W-1, i+1, W-1))

    return op


def f(H, W, a):
    """
    縦H行 横W列に区切られたマス目があり、
    上から i番目、左から j列目のマス: マス (i, j)
    マス (i, j) には aij枚のコイン

    あなたは以下の操作を何度でも行うことができます。
    操作:
        まだ選んだことのないマスのうち 1枚以上のコインが置かれているマスを 1つ選び、
        そのマスに置かれているコインのうち 1枚を上下左右に隣接するいずれかのマスに移動する
    偶数枚のコインが置かれたマスの数を最大化

    [考察]
    制約の数値が小さい
    奇数枚から奇数枚にコインを移したい
    2->2: 1, 3   2->0枚
    2->1: 1, 2   1->1枚
    1->2: 0, 3   1->1枚
    1->1: 0, 2   0->2枚

    1回しか動かせない
        1 or 2に限定してよいのでは
    startはどこからがよいのか？
        角４つから？
        全マスから？

    2を偶数、3を奇数としたときのパターン
        0: 222
        1: 223
        2: 232
        3: 233 -> 224
        4: 322
        5: 323 -> 233 -> 224
        6: 332 -> 242
        7: 333 -> 243

    その他パターン
        3223: 不変
        3232: 不変
        3333: 不変

    パターン5を優先？
    横だけじゃなくて、
        ＿＿上
        ＿上上上
        左左・右右
        ＿下下下
        ＿＿下
    """
    even = 0
    for line in a:
        even += sum(1 for x in line if a % 2 == 0)

    even = max(even, 0)
    ans = []
    return ans


def TLE(H, W, a):
    op2 = [[0] * W for _ in range(H)]
    op = []
    for i in range(H):
        for j in range(W):
            x = a[i][j]
            if x % 2 == 0:
                continue

            if j+1 < W and a[i][j+1] % 2 == 1:
                a[i][j] -= 1
                a[i][j+1] += 1
                op.append((i, j, i, j+1))
            elif j+2 < W and a[i][j+2] % 2 == 1:
                a[i][j] -= 1
                a[i][j+2] += 1
                op.append((i, j, i, j+1))
                op.append((i, j+1, i, j+2))
            elif i+1 < H and a[i+1][j] % 2 == 1:
                a[i][j] -= 1
                a[i+1][j] += 1
                op.append((i, j, i+1, j))
            elif i+2 < H and a[i+2][j] % 2 == 1:
                a[i][j] -= 1
                a[i+2][j] += 1
                op.append((i, j, i+1, j))
                op.append((i+2, j, i+2, j))

    return op


if __name__ == '__main__':
    main()
