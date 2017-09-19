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

# char <-> int
assert chr(49) == "1"
assert chr(65) == "A"
assert chr(97) == "a"
assert ord("A") == 65
assert ord("a") == 97

# bit
assert 32 << 2 == 128
assert 128 >> 2 == 32
