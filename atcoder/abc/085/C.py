def main():
    N, Y = map(int, input().split())

    #TLE(N, Y)
    exhaustive_search(N, Y)


def TLE(N, Y):
    # 2000**3 => 8 * 10 * 9:TLE
    for m in range(N, -1, -1):
        for g in range(N - m, -1, -1):
            for s in range(N - m - g, -1, -1):
                if m + g + s == N and \
                        m * 10000 + g * 5000 + s * 1000 == Y:
                    print(m, g, s)
                    return

    print(-1, -1, -1)


def exhaustive_search(N, Y):
    # 2000**2 => 4 * 10 * 6:Not TLE
    for m in range(N + 1):
        for g in range(N + 1):
            s = N - m - g
            #print(m, g, s)
            if 0 <= s <= N and \
                    m + g + s == N and \
                    m * 10000 + g * 5000 + s * 1000 == Y:
                print(m, g, s)
                return

    print(-1, -1, -1)


def no_submit(N, Y):
    """
    お金ベースで計算したダメな?例
    """
    # お札の最適化
    s = Y % 5000 // 1000
    g = (Y % 10000) // 5000
    m = Y // 10000

    # 10000円両替 + 5000円両替の組合せ
    for i in range(m + 1):
        # 10000両替
        _m = m - i
        if _m != 14:
            continue
        for j in range(g + 1):
            # 5000両替
            _g = g - j
            _s = s + j * 5

            # 10000円の両替パターン
            for k in range(i + 1):
                gg = _g + k * 2
                print("A:", _m, gg, _s)
                if _m + gg + _s == N:
                    print(_m, gg, _s)
                    return

                # 10000 to 5000 + 1000 * 5
                gg = _g + k
                ss = _s + k * 5
                print("B:", _m, gg, ss)
                if _m + gg + ss == N:
                    print(_m, gg, ss)
                    return

                # 10000 to 1000 * 10
                ss = _s + k * 10
                print("C:", _m, _g, ss)
                if _m + _g + ss == N:
                    print(_m, _g, ss)
                    return

    print(-1, -1, -1)

if __name__ == '__main__':
    main()
