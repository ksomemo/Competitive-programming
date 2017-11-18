def main():
    H, W = map(int, input().split())
    c = [
        list(map(int, input().split()))
        for _ in range(10)
    ]

    # c から最小魔力テーブルの算出
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c1 = c[i][j]
                c2 = c[i][k] + c[k][j]
                if c1 > c2:
                    c[i][j] = c2

    ans = 0
    for _ in range(H):
        for a in map(int, input().split()):
            if a != -1:
                ans += c[a][1]

    print(ans)

if __name__ == '__main__':
    main()
