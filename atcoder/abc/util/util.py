"""
utility

syntax check by py_compile module
    python -m py_compile util.py
"""
# queue関連:
# => http://n-knuu.hatenablog.jp/entry/2015/05/30/183718
# heapq: priority queue
# dequeu: fast queue
import heapq
from bisect import bisect
from collections import deque, Counter
from itertools import (
    # 直積/順列/組合せ/重複組合せ
    product,
    permutations,
    combinations,
    combinations_with_replacement
)
from statistics import mean, median, mode
from math import factorial, hypot as euclidean_dist

try:
    # py3.5
    from math import gcd
except:
    from fractions import gcd

try:
    # py3.6
    from statistics import harmonic_mean
except:
    def harmonic_mean(data):
        from fractions import Fraction
        n = len(data)
        d = sum(Fraction(1, Fraction(x)) for x in data)
        return float(n / d)


def lcm(x, y):
    return x * y // gcd(x, y)


def input_int():
    return int(input())


def input_list():
    return input().split()


def input_int_list():
    return list(map(int, input_list()))


def print_err(*args, **kwargs):
    """for debug"""
    import sys
    print(*args, file=sys.stderr, **kwargs)


def mid(low, high, overflow=True):
    """
     l + (h - l) / 2
    (2l + h - l) / 2
    (l + h) / 2
    """
    if overflow:
        return low + (high - low) // 2
    else:
        return (low + high) // 2


def dir4(x, y):
    dx = (0, 1, 0, -1)
    dy = rot_right_list(dx, 1)
    # => (-1, 0, 1, 0)

    for _dx, _dy in zip(dx, dy):
        new_x = x + _dx
        new_y = x + _dy
        # 盤面からはみ出てout of indexにならないように判定
        # x_min <= new_x <= x_max


def dir8(x, y):
    d = (0, 1, -1)
    for dx in d:
        for dy in d:
            if (dx, dy) == (0, 0):
                continue


def rot_right_list(a, n, use_dq=False):
    """
    shiftした組合せを見たい時などに利用

    left: (1,2,0)
    src:  (0,1,2)
    right:(2,0,1)
    """
    if use_dq:
        q = deque(a)
        q.rotate(n)
        return list(q)
    else:
        # n>0:left, n<0:right
        n = -n
        return a[n:] + a[:n]


# char <-> int
assert chr(49) == "1"
assert chr(65) == "A"
assert chr(97) == "a"
assert ord("A") == 65
assert ord("a") == 97

# bit
assert 32 << 2 == 128
assert 128 >> 2 == 32
