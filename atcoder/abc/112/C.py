def main():
    """
    1 <= N      <= 100
    0 <= xi, yi <= 100
    0 <= hi     <= 10^9
    """
    N = int(input())
    x, y, h = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    ans = no_sub(x, y, h)
    print(*ans)


def h_H(cx, cy, x, y):
    return - abs(x - cx) - abs(y - cy)


def no_sub(x, y, h):
    max_h = -1
    ans = None
    dict_h = {(_x, _y): _h for _x, _y, _h in zip(x, y, h)}
    for _x, _y, _h in zip(x, y, h):
        for cx in range(1, 100+1):
            for cy in range(1, 100+1):
                tmp = h_H(cx, cy, _x, _y)
                pos = (cx, cy)
                H = _h - tmp
                if pos in dict_h and H != dict_h[pos]:
                    continue

                if H > max_h:
                    max_h = H
                    ans = _x, _y, H

                # print((_x, _y), (cx, cy), _h, tmp, sep="\t")

    return ans


def f2(x, y, h):
    chs = []
    for _x, _y, _h in zip(x, y, h):
        for cx in range(0, 100 + 1):
            for cy in range(0, 100 + 1):
                tmp = h_H(cx, cy, _x, _y)
                print((_x, _y), (cx, cy), _h, tmp, sep="\t")

    return 1


if __name__ == '__main__':
    main()
