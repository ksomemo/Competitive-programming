def main():
    N = int(input())
    txy = [
        tuple(map(int, input().split()))
        for _ in range(N)
    ]

    _t, _x, _y = 0, 0, 0
    for t, x, y in txy:
        ok = False
        diff_t = t - _t
        diff_x = x - _x
        diff_y = y - _y

        dx = abs(diff_x)
        dy = abs(diff_y)
        if diff_t >= dx + dy:
            rem = dx + dy - diff_t
            if rem % 2 == 0:
                ok = True
                _t, _x, _y = t, x, y

        if not ok:
            print("No")
            return

    print("Yes")

if __name__ == '__main__':
    main()
