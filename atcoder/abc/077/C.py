import bisect


def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted(map(int, input().split()))

    ans = 0
    for b in B:
        na = bisect.bisect_left(A, b)
        nc = N - bisect.bisect_right(C, b)
        ans += na * nc

    print(ans)


def TLE(N, A, B, C):
    # a<b<c となる並べ方の数
    # b<c となる並べ方の数、１つずつに対してN個調べるO(N^2) => すでにOver => pypy
    # b M個となったとき (b_c_i - b_c_m) を保持する
    # a<b となる並べ方の数、１つずつに対してN個調べるO(M*N)
    # b L個となったとき (b_a_i - b_a_m) を保持する (b_cと対応付ける)

    ans = 0
    for b in B:
        less_b_count = sum(1 for a in A if a < b)
        if less_b_count > 0:
            over_b_count = sum(1 for c in C if b < c)
            ans += less_b_count * over_b_count

    print(ans)


def my_bisect_LR(a, x, right=True, verbose=False):
    """https://github.com/python/cpython/blob/3.6/Lib/bisect.py 
    """
    low = 0
    hi = len(a)

    if verbose:
        print("my_bisect", a, x)
        print("right:", right)

    while low < hi:
        mid = (low + hi) // 2
        if verbose:
            print(low, hi, mid)
        if right:
            if x < a[mid]:
                hi = mid
            else:
                low = mid + 1
        else:
            if a[mid] < x:
                low = mid + 1
            else:
                hi = mid

    return low

if __name__ == '__main__':
    main()
