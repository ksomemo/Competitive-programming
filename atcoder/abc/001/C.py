def main():
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "test":
        test_example()
    else:
        deg, dis = map(int, input().split())

        d, w = solve(deg, dis)
        print(d, w)


def direction(deg):
    d_name = [
        "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
    ]
    # 3600 / 16 => 225
    # NNE (北北東): 11.25 度以上 33.75 度未満
    d = d_name[0]
    for i, name in enumerate(d_name, 1):
        if deg * 10 < i * 2250 - 1125:
            d = name
            break

    return d


def w_power(dis):
    # 5: 10.7以下
    # 6: 10.8以上
    # 小数第 2 位を四捨五入 より
    # であるが 10.73333は 5
    # 風力N-min未満なら風力N-1とする
    ws = [
        0.3, 1.6, 3.4, 5.5, 8.0,
        10.8, 13.9, 17.2, 20.8, 24.5,
        28.5, 32.7, float("inf"),
    ]
    for i, w in enumerate(ws):
        if _round(dis / 60, 1) < w:
            W = i
            break

    return W


def solve(deg, dis):
    d = direction(deg)
    W = w_power(dis)

    bef_d = d
    if W == 0:
        d = "C"

    return (d, W)


def test_example():
    in_out = [
        ((2750, 628), ("W", 5)),
        ((161, 8), ("C", 0)),
        ((3263, 15), ("NNW", 1)),
        ((1462, 1959), ("SE", 12)),
        ((1687, 1029), ("SSE", 8)),
        ((2587, 644), ("WSW", 5)),
        ((113, 201), ("NNE", 3)),
        ((2048, 16), ("SSW", 1)),
    ]

    for p_num, (i, o) in enumerate(in_out, 1):
        res = solve(*i)
        print(p_num, res == o,
              "res:{}".format(res),
              "expected:{}".format(o), sep="\t")


def _round(x, d=0):
    """
    https://qiita.com/sak_2/items/b2dd8bd1c4e4b0788e9a#comment-ed35e21b3969ca6ae77e
    """
    p = 10 ** d
    return (x * p * 2 + 1) // 2 / p


def _round_decimal(x, d=0, asfloat=True):
    """
    https://stackoverflow.com/questions/21839140/python-3-rounding-behavior-in-python-2
    https://docs.python.org/ja/3.6/library/decimal.html

    for float in python3

        f(1.255,  d=2) # => 1.25  orz
        f(1.2555, d=2) # => 1.26  ok
        f(1.2555, d=3) # => 1.256 ok

    1.255 * 10
    # => 12.549999999999999

    1.255 + sys.float_info.epsilon
    # => 1.2550000000000001

    % ~/.pyenv/versions/2.7.13/bin/python -c "print(round(1.255, 2))"
    # => 1.25
    """
    import decimal
    x = decimal.Decimal(x)
    d = "1e-{}".format(d)
    r = x.quantize(decimal.Decimal(d), rounding=decimal.ROUND_HALF_UP)

    if asfloat:
        return float(r)
    else:
        return r


if __name__ == '__main__':
    main()
