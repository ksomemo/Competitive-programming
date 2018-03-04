def main():
    N, K = map(int, input().split())
    x, y = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    TLE(N, K, x, y)


def TLE(N, K, x, y):
    """
    TLEのため、考察はpypy3のD directoryに移行
    codeの見た目のためにgeneratorを使ったが遅いので愚直にloopにしたがTLE
    解説の累積和をあとで試す
    """
    sorted_x = sorted(x)
    sorted_y = sorted(y)
    ans = (sorted_x[-1] - sorted_x[0]) * (sorted_y[-1] - sorted_y[0])
    for xi in range(N):
        for xj in range(xi + 1, N):
            for yi in range(N):
                for yj in range(yi + 1, N):
                    min_x, max_x = sorted_x[xi], sorted_x[xj]
                    min_y, max_y = sorted_y[yi], sorted_y[yj]
                    contains_count = 0
                    for x3, y3 in zip(x, y):
                        if min_x <= x3 <= max_x and min_y <= y3 <= max_y:
                            contains_count += 1
                    if contains_count >= K:
                        s = (max_x - min_x) * (max_y - min_y)
                        ans = min(ans, s)

    print(ans)


if __name__ == "__main__":
    main()
