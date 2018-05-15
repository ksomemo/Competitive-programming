N = int(input())
mains = []
subs = []
for m, s in [map(int, input().split()) for _ in range(N)]:
    mains.append(m)
    subs.append(s)

import math


def multiply(g, h):
    for i in range(len(g)):
        for j in range(len(h)):
            f[i+j] += g[i] * h[j]
    return f


def pow_2_at_least(n):
    p = 1
    while p < n:
        p = p * 2
    return p


def dft(f, n, inv=False):
    if n == 1:
        return [f[0]]
    # 奇数と偶数に分ける
    f0 = [f[2*i + 0] for i in range(n // 2)]
    f1 = [f[2*i + 1] for i in range(n // 2)]

    # 分けたものに対してDFT
    f0 = dft(f0, n // 2, inv=inv)
    f1 = dft(f1, n // 2, inv=inv)

    # ζ(ze-ta) = e^(2 * pi * √(-1) / n)
    # e^(iθ) = cosθ + isinθ
    zeta = complex(math.cos(2 * math.pi / n), math.sin(2 * math.pi / n))
    pow_zeta = 1
    if inv:
        zeta = 1 / zeta
    for i in range(n):
        f[i] = f0[i % (n // 2)] + pow_zeta * f1[i % (n // 2)]
        pow_zeta *= zeta
    return f


def padding_zero(xs, n):
    return xs + [0] * (n - len(xs))


def multiply2(g, h):
    # 係数の数を求めて足りない係数を補完する
    n = pow_2_at_least(len(g) + len(h) + 1)
    g2 = padding_zero(g, n)
    h2 = padding_zero(h, n)

    # それぞれDFTをして、その結果同士の係数をかけて畳み込み
    gg = dft(g2, n)
    hh = dft(h2, n)
    ff = [gg[i] * hh[i] for i in range(n)]

    # DFTの数の逆数をNで割る
    return [c / n for c in dft(ff, n, inv=True)]

#N = 4
#mains = [1,2,3,4]
#subs = [1,2,4,8]


result = multiply2(mains, subs)
print(0)
for c in result[0:2*N-1]:
    print(int(round(c.real)))
