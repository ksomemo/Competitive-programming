import cmath
import numpy as np


def pow_2_at_least(n):
    p = 1
    while p < n:
        p = p * 2
    return p


def padding_zero(xs, n):
    return xs + [0] * (n - len(xs))


def omega(p, q):
    return cmath.exp((2.0 * cmath.pi * 1j * q) / p)


def fft(signal):
    n = len(signal)
    if n == 1:
        return signal
    Feven = fft([signal[i] for i in range(0, n, 2)])
    Fodd = fft([signal[i] for i in range(1, n, 2)])

    combined = [0] * n
    for m in range(n // 2):
        combined[m] = Feven[m] + omega(n, -m) * Fodd[m]
        combined[m + n // 2] = Feven[m] - omega(n, -m) * Fodd[m]

    return combined


def ifft(signal):
    timeSignal = fft([x.conjugate() for x in signal])
    return [x.conjugate()/len(signal) for x in timeSignal]


def multiply2(g, h):
    # 係数の数を求めて足りない係数を補完する
    n = pow_2_at_least(len(g) + len(h) + 1)
    g2 = padding_zero(g, n)
    h2 = padding_zero(h, n)

    # それぞれDFTをして、その結果同士の係数をかけて畳み込み
    gg = fft(g2)
    hh = fft(h2)
    ff = [gg[i] * hh[i] for i in range(n)]

    # DFTの数の逆数をNで割る
    return ifft(ff)


N = 10000
mains = list(range(1, N))
subs = list(range(1, N*2, 2))

result = multiply2(mains, subs)
print(0)
for c in result[0:2*N-1]:
    print(int(round(c.real)))
