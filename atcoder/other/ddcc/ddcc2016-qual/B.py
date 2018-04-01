import math


def main():
    R, N, M = map(int, input().split())

    AC(R, N, M)


def AC(R, N, M):
    mid = N / 2

    def my_x(y):
        """
        midを原点としてyを決める
            分割によってRを基準できないため
        R=1の円にするため、midで正規化
        """
        _y = abs(mid - y) / mid
        theta = math.asin(_y)
        cosx = math.cos(theta)
        return R * 2 * cosx

    def editorial_x(y):
        """
        半径^2=求める線の長さ^2 + 中心からの距離^2
        """
        _y = R * abs(mid - y) / mid
        return 2 * math.sqrt(R**2 - _y ** 2)

    def x(y, editorial):
        if editorial:
            return editorial_x(y)
        else:
            return my_x(y)

    ans = 0
    editorial = True
    for y1 in range(1, N + M):
        y2 = y1 - M
        c1, c2 = 0, 0
        if 1 <= y1 <= N - 1:
            c1 = x(y1, editorial)
        if 1 <= y2 <= N - 1:
            c2 = x(y2, editorial)

        ans += max(c1, c2)

    # print(ans)
    print("{:.6f}".format(ans))


if __name__ == '__main__':
    main()
