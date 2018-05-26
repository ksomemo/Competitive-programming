def main():
    x1, y1, r = map(int, input().split())
    x2, y2, x3, y3 = map(int, input().split())

    # rect in circle
    if all([
        in_circle(x2, y2, r, x1, y1),
        in_circle(x2, y3, r, x1, y1),
        in_circle(x3, y2, r, x1, y1),
        in_circle(x3, y3, r, x1, y1),
    ]):
        print("YES")
        print("NO")
        return

    # circle in rect
    if all([
        in_rect(x1-r, y1, x2, y2, x3, y3),
        in_rect(x1+r, y1, x2, y2, x3, y3),
        in_rect(x1, y1-r, x2, y2, x3, y3),
        in_rect(x1, y1+r, x2, y2, x3, y3),
    ]):
        print("NO")
        print("YES")
        return

    print("YES")
    print("YES")


def dist(x1, y1, x2, y2):
    """ユークリッド距離
    """
    # autopep8 chenge to `f=lambda: 0` to `def f(): return 0``
    def sqrt(x): return x ** 0.5
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def in_circle(x, y, r, ox, oy):
    d = dist(x, y, ox, oy)
    return d <= r


def in_rect(x, y, x1, y1, x2, y2):
    return (x1 <= x <= x2) and (y1 <= y <= y2)


if __name__ == '__main__':
    main()
