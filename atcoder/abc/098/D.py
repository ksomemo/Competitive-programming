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

    editorial(N, A)


def editorial(N, A):
    """
    a + b − (a xor b) = 2 × (a and b)
    （ただしここで andはビットごとの論理積を表す）
    とは？

    xy|xor|(x xor y) xor y
    00|  0|0
    01|  1|0
    10|  1|1
    11|  0|1

    計算量を減らすための工夫
    しゃくとり法
    累積和, 累積XOR
    """
    #ans = shakutori(N, A)
    ans = bin_search_TLE(N, A)
    print(ans)


def bin_search_TLE(N, A):
    N_BIT = 20
    b = [
        [0] * (N+1)
        for _ in range(N_BIT)
    ]
    # bitごとの累積和
    for j in range(N_BIT):
        for i in range(N):
            x = (A[i] >> j) & 1
            b[j][i+1] = x + b[j][i]

    import bisect
    ans = 0
    for i in range(N):
        tmp = float("inf")
        for j in range(N_BIT):
            # 累積和の調整
            # i=1のとき i=0まで累積和+1がi=1以降では許容される
            a = 1 + b[j][i]
            # 0 to N-1ではなく、0 to Nなので -1 と i+1以降なので -i
            x = bisect.bisect_right(b[j], a)
            tmp = min(tmp, x - 1 - i)
        print("i:", i, "tmp:", tmp, "x:", x, "a:", a, "b[j][i]:", b[j][i], sep="\t")
        ans += tmp

    #return ans

    for x in b:
        print(*x)


def shakutori(N, A):
    """しゃくとり法
    """
    ans = 0
    right = 0
    _sum = 0
    for left in range(N):
        # 右の限界判定, rightを進めたときの条件判定
        while right < N and (_sum ^ A[right]) == (_sum + A[right]):
            # 進めたときの状態変化
            _sum += A[right]
            right += 1

        # 条件を満たす範囲
        ans += right - left

        if left == right:
            # 詰まっているので、条件判定前に戻す必要なし
            right += 1
        else:
            # 右を右へずらさず左を右へずらすので、条件判定前に戻す
            _sum -= A[left]

    return ans


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
