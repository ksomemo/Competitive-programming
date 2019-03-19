import math


def main():
    N = int(input())
    TA = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    # ans = f(N, TA)
    ans = editorial(N, TA)
    print(ans)


def test_ceil_mod():
    """https://stackoverflow.com/questions/14822184/is-there-a-ceiling-equivalent-of-operator-in-python
    >>> import math
    >>> math.ceil(11520000000000000102.9) == 11520000000000000000
    True
    """
    for i in range(1, 10 ** 5):
        for j in range(1, 10 ** 2):
            assert math.ceil(i / j) == (i // j + (i % j != 0)), (i, j)
            assert math.ceil(j / i) == (j // i + (j % i != 0)), (j, i)


def editorial(N, TA):
    A, B = 1, 1
    for x, y in TA:
        # n = max(math.ceil(A / x), math.ceil(B / y))
        n = max(A // x + (A % x != 0),
                B // y + (B % y != 0))
        A, B = n * x, n * y

    ans = A + B
    return ans


def f(N, TA):
    nt, na = TA[0]
    bef_t, bef_a = nt, na
    for t, a in TA[1:]:
        if (bef_t, bef_a) == (t, a):
            # 変化なし
            pass
        elif (t, a) == (1, 1):
            # 同票なので、合わせる
            m = max(nt, na)
            nt, na = m, m
        elif t == 1:
            na = nt * a
        elif a == 1:
            nt = na * t
        elif (bef_t, bef_a) == (1, 1):
            # 1:1 -> 3,3
            # 3:2 -> 3,2(NG) 6:4 -> 6,4(OK)
            i = 1
            while nt <= t or na <= a:
                nt, na = t * i, a * i
                i += 1

        elif bef_t == t and bef_a < a:
            # 2:3 -> 4,6
            # 2:7 -> 4,14
            na = na // bef_a * a
        elif bef_t < t and bef_a == a:
            nt = nt // bef_t * t
        else:
            aa = na // a
            tt = nt // t
            if aa > 0 and tt > 0 and aa == tt:
                pass
            else:
                x = nt % t
                y = na % a
                if x != 0:
                    add_t = t - x
                    nt += add_t
                if y != 0:
                    add_a = a - y
                    na += add_a
                aa = na // a
                tt = nt // t
                if aa > tt:
                    nt = t * aa
                elif aa < tt:
                    na = a * tt
            # (nt + x): (na + y) = t: a
            # na * t + y * t = (nt + x) * a
            #          y * t = (nt + x) * a     - na * t
            #          y     = (nt + x) * a / t - na
            # x,y >= 0
            # (nt + x) / t is int
            #     a    / t is int
        bef_t, bef_a = t, a
        # print(nt, na, (t, a))

    ans = nt + na
    return ans


if __name__ == '__main__':
    main()
