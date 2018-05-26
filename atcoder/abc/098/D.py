def main():
    """
    1 <= N <= 2 * 10^5
    0 <= Ai <= 2^20

    1 <= l <= r <= N

       Al xor Al_1 xor ... xor Ar
    == Al  +  Al_1  +  ... xor Ar
    """
    N = int(input())
    *A, = map(int, input().split())

    TLE(N, A)

def f(N, A):
    """
    入力例1

    (1,r)=(1,2) => [2,5]
    2: 010
    5: 101
    ------
    7: 111

    XOR: 0が1or偶数個,1が1つ? すべてのbitが立つ?
    """
    pass


def TLE(N, A):
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            a1 = A[i:j]
            s = sum(a1)

            x = a1[0]
            for y in a1[1:]:
                x ^= y
            if x == s:
                ans += 1
            print((i, j), x, s, ans, a1, sep="\t")

    print(ans)

if __name__ == '__main__':
    main()
