def main():
    N = int(input())
    xy = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    ans = 0
    for i in range(N):
        for j in range(N):
            (x1, y1), (x2, y2) = xy[i], xy[j]
            ans = max(ans, dist(x1, y1, x2, y2))

    print(ans)


if __name__ == '__main__':
    main()
