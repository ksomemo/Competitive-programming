def main():
    H, W = map(int, input().split())
    A = [
        list(input())
        for _ in range(H)
    ]

    editorial(H, W, A)


def editorial(H, W, A):
    """
    最短経路と同じ#の個数
    多ければ寄り道している
    """
    count = sum(a.count("#") for a in A)

    if count == H + W - 1:
        print("Possible")
    else:
        print("Impossible")


def AC(H, W, A):
    # 2 <= H,W <= 8 より右下全列挙でもいけそう
    # H+W-2歩く(0,0からのため)、max:2 ** 14 = 16384
    # x:0, y:1
    p = [0] * (H + W - 2)

    def dfs(i):
        if i == H + W - 2:
            # 歩き方はあり得るか
            if p.count(1) != H-1 or p.count(0) != W-1:
                return False

            b = [
                ["."] * W
                for _ in range(H)
            ]
            x, y = (0, 0)
            b[0][0] = "#"
            for c in p:
                if c == 1:
                    y += 1
                else:
                    x += 1
                b[y][x] = "#"

            return A == b

        p[i] = 0
        if dfs(i + 1):
            return True
        p[i] = 1
        if dfs(i + 1):
            return True

        return False

    if dfs(0):
        print("Possible")
    else:
        print("Impossible")


if __name__ == '__main__':
    main()
