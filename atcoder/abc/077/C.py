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

if __name__ == '__main__':
    main()
