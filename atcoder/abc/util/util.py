import heapq
from bisect import bisect
from collections import deque, Counter
from itertools import permutations, combinations, product
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
