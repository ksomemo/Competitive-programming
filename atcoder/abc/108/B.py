import pytest


def main():
    x1, y1, x2, y2 = map(int, input().split())

    ans = editorial(x1, y1, x2, y2)
    print(*ans)


@pytest.mark.randomize(x1=int, y1=int, x2=int, y2=int,
                       min_num=-(10 ** 2), max_num=10 ** 2)
def test_ans(x1, y1, x2, y2):
    assert editorial(x1, y1, x2, y2) == twi(x1, y1, x2, y2)


def twi(x1, y1, x2, y2):
    """
                [2]
              (-1,+1)
                 |   
    -[3]:(-2, 0)-+-( 0, 0):[1]-
                 | 
              (-1,-1)
                [4]
 
    dx = -1
    dy = +1
                [2]
              (+2,+3)
                 |   
    -[3]:(+1,+2)-+-(+3,+2):[1]-
                 | 
              (+2,+1)
                [4]
 
    https://twitter.com/akensho/status/1035924165205716992
    https://twitter.com/hogeover30/status/1035903937830764545
    """
    import math
    cos90 = int(math.cos(math.pi / 2))
    sin90 = int(math.sin(math.pi / 2))

    x = x2 - x1
    y = y2 - y1
    x4 = x * cos90 - y * sin90 + x1
    y4 = x * sin90 + y * cos90 + y1

    x = x1 - x4
    y = y1 - y4
    x3 = x * cos90 - y * sin90 + x4
    y3 = x * sin90 + y * cos90 + y4

    return x3, y3, x4, y4


def editorial(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1

    x3 = x2 - y
    y3 = y2 + x
    x4 = x1 - y
    y4 = y1 + x

    return x3, y3, x4, y4


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
