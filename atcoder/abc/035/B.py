from collections import Counter


def main():
    S = input()
    T = int(input())

    c = Counter(S)
    # c[not in key] => 0
    L = c.get("L", 0)
    R = c.get("R", 0)
    U = c.get("U", 0)
    D = c.get("D", 0)
    x = R - L
    y = U - D
    q = c.get("?", 0)

    if T == 1:
        # max
        m = abs(x) + abs(y) + q
    else:
        # min
        # 調整後x,yの符号無視
        _x = min(abs(x), q)
        q -= _x
        x = abs(x) - _x

        _y = min(abs(y), q)
        q -= _y
        y = abs(y) - _y

        m = abs(x) + abs(y) + (q % 2)

    print(m)

if __name__ == '__main__':
    main()
