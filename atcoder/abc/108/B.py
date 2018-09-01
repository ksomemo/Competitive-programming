def main():
    x1, y1, x2, y2 = map(int, input().split())

    x3, y3, x4, y4 = f(x1, y1, x2, y2)
    print(x3, y3, x4, y4)


def f(x1, y1, x2, y2):
    if x1 == x2:
        # print("x")
        y3 = y2
        y4 = y1
        x3 = x1 - abs(y2)
        x4 = x3
    elif y1 == y2:
        # print("y")
        x3 = x2
        x4 = x1
        y3 = y1 - abs(x2)
        y4 = y3
    else:
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        d = dx + dy
        if y2 > y1 and x2 < x1:
            # 右1,上2
            x3, y3, x4, y4 = \
                x1 - d, y2 - dx, x1 - dy, y2 - d

        elif y2 < y1 and x2 < x1:
            # 上1,左2
            x3, y3, x4, y4 = \
                x2 - dy, y1 - d, x2 + d, y1 + dx

        elif y2 < y1 and x2 > x1:
            # 左1,下2
            x3, y3, x4, y4 = \
                x1 + d, y2 + dx, x1 + dy, y2 + d

        elif y2 > y1 and x2 > x1:
            # 下1,右2
            x3, y3, x4, y4 = \
                x2 - dy, y1 + d, x2 - d, y1 + dx

    return x3, y3, x4, y4


if __name__ == '__main__':
    main()
