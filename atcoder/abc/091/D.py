from bisect import bisect_left, bisect_right


def main():
    """
    N=2*10^5

    http://hamayanhamayan.hatenablog.jp/entry/2017/05/20/145021
        競技プログラミングにおけるXOR問題まとめより
        性質3:ある数xのb番目のビットが1である
            <=> x mod 2^(b+1) ≧ 2^b
        方針1:xor計算は各ビットで独立なので別々に計算

    解説動画より(解説pdf簡素だったので)
        k-bit目の値が0/1 を各kについて求める
        ai+bj のうち、k-bit目が1であるものの個数は何個か？()
            それの偶奇で

        2^k = T としたとき

        modをとって 0 <= ai,bi < 2T の範囲に変更する
        すると 0 <= ai+bj <= 4T になる
    """
    N = int(input())
    # to list
    *A, = map(int, input().split())
    *B, = map(int, input().split())

    # TLE(N, A, B)
    editorial_TLE_pypy(N, A, B)


def f(N, A, B):
    pass


def editorial_TLE_pypy(N, A, B):
    """
    参考

    https://beta.atcoder.jp/contests/arc092/submissions/2225586
    https://beta.atcoder.jp/contests/arc092/submissions/2224269
    """
    ans = 0
    # 2^28 + 2^28 = 2^29 より
    n_bit = 29
    for i in range(n_bit + 1):
        t = 1 << i
        t2 = t << 1
        # b % i == b & (i - 1) => 2^m - 1は全ビット立っているから
        mod = sorted(b & (t2 - 1) for b in B)
        # mod = sorted([b % t2 for b in B])

        count = 0
        for a in A:
            da = a % t2

            # a固定(Tと合わせてbと比較)
            t1_count = bisect_left(mod, t - da)
            t2_count = bisect_left(mod, t2 - da)
            t3_count = bisect_left(mod, t * 3 - da)

            count += N - t3_count + t2_count - t1_count

        if count & 1 == 1:
            ans += 1 << i

    print(ans)


def fb(x, b):
    """
    format Decimal to Binary, b-bit is 1 => True

    0b11111=31
    2^4=16で割った余りは
    0b01111=15 (0-15)
    10で割った余りと同様にその桁以降の数になるので,難しいことではなく2進数版であるだけ
    """
    xb = format(x, "b")
    pow_b = 2 ** b
    b_is_1 = x % (2 * pow_b) >= pow_b
    return xb, b_is_1


def fb_loop(k):
    """
    0 to (2**k) * 4 - 1の範囲
    f(1): 0-indexedにおいて1bit目が1かどうか
    0  0000000  False
    1  0000001  False
    2  0000010  True
    3  0000011  True
    4  0000100  False
    5  0000101  False
    6  0000110  True
    7  0000111  True

    [ 0,  T): 0
    [ T, 2T): 1
    [2T, 3T): 0
    [3T, 4T): 1
    """
    t = 2 ** k
    for i in range(t * 4):
        print(i, "{0:07b}".format(i, "b"), i % (t*2) >= t, sep="\t")


def TLE(N, A, B):
    A = list(A)
    B = list(B)

    ans = 0
    for a in A:
        for b in B:
            ans ^= a + b

    print(ans)


if __name__ == '__main__':
    main()
