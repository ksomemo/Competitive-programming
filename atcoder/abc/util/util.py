"""
utility

syntax check by py_compile module
    python -m py_compile util.py
"""
# queue関連:
# => http://n-knuu.hatenablog.jp/entry/2015/05/30/183718
# heapq: priority queue
# dequeu: fast queue
import sys
import math
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
    # 最大公約数: greatest common divisor
    # py3.5+
    from math import gcd
except ImportError:
    from fractions import gcd

try:
    # py3.6+
    from statistics import harmonic_mean
except ImportError:
    def harmonic_mean(data):
        from fractions import Fraction
        n = len(data)
        d = sum(Fraction(1, Fraction(x)) for x in data)
        return float(n / d)


def my_gcd_rec(a, b):
    c = a % b
    if c == 0:
        return b
    # a < bのとき, bでは割れないため単純に入れ替えになるため大小判定不要
    return my_gcd_rec(b, c)


def my_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    # b == 0, ans==前のloopのb より、今のaを返す
    return a


def lcm(x, y):
    """最小公倍数: least common multiple"""
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


def eratosthenes(N):
    """エラトステネスの篩

    TODO: もっと速い方法(下記と基本同じなので問題なさそう)
    競プロの強い人のPython実装
        https://ideone.com/ZNfMXw
        https://twitter.com/not_522/status/979330568960712705
    """
    is_prime = [True for _ in range(N + 1)]
    is_prime[0] = False
    is_prime[1] = False
    max_prime = int(math.sqrt(N))
    for n in range(2, max_prime + 1):
        if is_prime[n]:
            # n-1までは判定済みのため除外されている
            # => max_prime導入も同じ理由
            for i in range(n * n, N + 1, n):
                is_prime[i] = False
    return is_prime


def factorize(N):
    """素因数分解

    TODO: もっと速い方法
    素因数がある場合は範囲をsqrtで狭められるが、ない場合愚直に探してしまう
    N以下の素数を見つけて、それだけで対応すれば速いはず
    """
    factors = []
    while True:
        if N % 2 == 0:
            factors.append(2)
            N //= 2
        else:
            break
    m = int(math.sqrt(N))
    i = 3
    while i <= m:
        add = False
        while True:
            if N % i == 0:
                factors.append(i)
                N //= i
                add = True
            else:
                break
        if add:
            m = int(math.sqrt(N))
        i += 2
    if N > 1:
        factors.append(N)
    return factors


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


def idx_cond_loop(x, n, interval, start):
    """ABC 001-C の風向条件判定 自作

    0 <= x < 60 のような一定範囲に対して、
    始点をずらしてからの等間隔に区切った時
    どの区間に所属するか

    0:       x < 10 or x >= 55
    1: 10 <= x < 25
    2: 25 <= x < 40
    3: 40 <= x < 55
    """
    ans = 0
    for i in range(n):
        if x < i * interval + start:
            ans = i
            break
    return ans


def idx_range(x, n, interval, start):
    """ABC 001-C の解説にあった計算式

    https://www.slideshare.net/chokudai/abc001

    x - y: x以上y未満
    start: 0    | start: 10
    interval: 15| interval: 15
    0:  0 - 15  |  0 - 10, 55 - 60
    1: 15 - 30  | 10 - 25
    2: 30 - 45  | 25 - 40
    3: 45 - 60  | 40 - 55
    """
    return (x + (interval - start)) // interval % n


def note_trigonometric_func():
    """
    三角関数と逆三角関数
    """
    pi_div_2 = math.asin(1)
    near_1 = math.sin(pi_div_2)


def run_perm(N, n_types):
    """
    全列挙
    """
    a = [0] * N

    def perm(i, n):
        if i == n:
            print(a)
            return
        for t in range(n_types):
            a[i] = t
            perm(i+1, n)
    perm(0, N)


def my_permutations(iterable, r=None):
    """
    https://docs.python.jp/3.6/library/itertools.html#itertools.permutations
    http://blog.shibayu36.org/entry/2016/12/21/081625
    http://jutememo.blogspot.jp/2008/09/python_29.html
    http://code.activestate.com/recipes/190465/
    """
    pass


def my_product(*iterables, repeat=1):
    pass


def my_combinations(iterable, r):
    pass


def _factorial(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def npr(n, r):
    if n < r:
        return 0
    a = 1
    for i in range(r):
        a *= n - i
    return a


def ncr(n, r):
    _npr = npr(n, r)
    if _npr == 0:
        return 0
    return _npr // _factorial(r)


def ncr2(n, r):
    if n < r:
        return 0
    f = factorial
    # rまでの並べ方について,組合せなので1/r
    return f(n) // f(n - r) // f(r)


def nhr(n, r):
    """combination with repetitions"""
    return ncr(n + r - 1, r)


def facotr_counts(M):
    """factorize とは違ってコンパクトにまとめた
    """
    i = 2
    rest_M = M
    counts = {}
    while i ** 2 <= rest_M:
        div_count = 0
        while rest_M % i == 0:
            div_count += 1
            rest_M //= i

        if div_count > 0:
            counts[i] = div_count

        i += 1

    if rest_M != 1:
        counts[rest_M] = 1

    return counts


def calc_comb(n, r, mod=10 ** 9 + 7):
    if r > n - r:
        return calc_comb(n, n - r)

    ans_mul = 1
    ans_div = 1

    for i in range(r):
        # n! / (n - r)!
        ans_mul = ans_mul * (n - i) % mod
        # r!
        ans_div = ans_div * (i + 1) % mod

    # k^(-1) ≡ k^(n-2) (mod n)
    return ans_mul * mod_pow(ans_div, mod - 2) % mod


def mod_pow(a, p, mod=10 ** 9 + 7):
    if p == 0:
        return 1

    if p % 2 == 0:
        half_p = p // 2
        half = mod_pow(a, half_p)
        return half ** 2 % mod
    else:
        return a * mod_pow(a, p - 1) % mod


def mod_pow_bit(a, p, mod=10 ** 9 + 7):
    """
    http://keita-matsushita.hatenablog.com/entry/2016/12/05/184011
    """
    ans = 1
    while p > 0:
        if (p & 1) == 1:
            ans = ans * a % mod

        a = a ** 2 % mod
        p >>= 1

    return ans


def mod_for_minus(x, m):
    """python では問題ないが、cppなどでは負に対応していない

    #include <iostream>
    using namespace std;

    int main() {
        int ans = ((-3 % 2) + 2) % 2;
        cout << "  -3 % 2           = " << (-3 % 2) << endl;
        cout << "  +3 % 2           = " << (+3 % 2) << endl;
        cout << "((-3 % 2) + 2) % 2 = " << ans << endl;
        // -1, 1, 1
        return 0;
    }
    """
    return (x % m + m) % m


def create_tables(N, MOD):
    """
    http://drken1215.hatenablog.com/entry/2018/06/08/210000
    """
    fact_mod = [0] * (N + 1)
    simod = [0] * (N + 1)
    fact_inv_mod = [0] * (N + 1)

    fact_mod[0] = fact_mod[1] = 1
    simod[0] = simod[1] = 1
    fact_inv_mod[0] = fact_inv_mod[1] = 1

    for i in range(2, N + 1):
        # 階乗の累積積
        fact_mod[i] = (fact_mod[i - 1] * i) % MOD

        # TODO: これはなにを意味するのか？
        simod[i] = MOD - simod[MOD % i] * (MOD // i) % MOD

        # 最終的に使いたい階乗の逆元 (mod)
        fact_inv_mod[i] = (fact_inv_mod[i - 1] * simod[i]) % MOD
        # TODO: inv 配列が確実に不要な場面 とは？ (ここでのsimod)
        # inv[n] を逆元計算によって計算しておく
        # finv[i-1] = finv[i] * i % MOD によって finv 配列を後ろから計算していく

    return fact_mod, fact_inv_mod


def comb_mod(N, R, fact_mod, fact_inv_mod, MOD):
    """
    組合せ nCr: n! / ((n-r)! * r!)
    上記のmodを逆元を使って表現

    f[n] * f[r] % MOD * f[n-r] % MOD 
    これのために事前にテーブルを作っていた
    """
    return fact_mod[N] * fact_inv_mod[N - R] * fact_inv_mod[R] % MOD


def comb_with_fermat(N, R, MOD):
    """フェルマーの小定理を用いてコンビネーションを計算する

    http://keita-matsushita.hatenablog.com/entry/2016/12/05/184011
    https://mathtrain.jp/fermat_petit
        pが素数, aが任意の自然数のとき
            競プロにおいて, p=10^9+7 よりpは素数
        a^p ≡ a (mod p)
            (a^p) % p = a % p
            なので modの世界とか言われてるはず

        a^(p-1) ≡ 1    (mod p)
        a^(p-2) ≡ a^-1 (mod p)
            a と pが互いに素: (a ⊥ p)

        この-1乗の部分にフェルマーの小定理を適用
        nCr = n! * ((n - r)!)^(-1) * (r!)^(-1)
        nCr (mod p)
            =  n! * ((n - r)!)^(-1) * (r!)^(-1) (mod p)

    https://www.youtube.com/watch?v=fYS-rAUSD5o
    http://drken1215.hatenablog.com/entry/2018/06/08/210000
    https://www37.atwiki.jp/uwicoder/pages/2118.html
        nCkについては、因幡めぐるちゃんが制約別３パターンをツイート
    """
    fact_mod, fact_inv_mod = create_tables(N + 100, MOD)
    ans = comb_mod(N, R, fact_mod, fact_inv_mod, MOD)
    ans %= MOD

    return ans


def my_divmod(x, y):
    a = x // y
    b = x - a * y
    return (a, b)


def bitesize(x):
    """
    "a": 50
    "ab": 51
    return sys.getsizeof(x)
    """


# char <-> int
assert chr(49) == "1"
assert chr(65) == "A"
assert chr(97) == "a"
assert ord("A") == 65
assert ord("a") == 97

# bit
assert 32 << 2 == 128
assert 128 >> 2 == 32
