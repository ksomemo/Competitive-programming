def main():
    """
    1 <= N <= 10^5
    1 <= K <= N
    |xi| <= 10^8
        -10^8 <= xi <= 10^8
    xs: sorted
    """
    N, K = map(int, input().split())
    * x, = map(int, input().split())
    # ans = WA(N, K, x)
    ans = editorial(N, K, x)
    print(ans)


def editorial(N, K, x):
    """
    start: 0
    all x >= 0, 近傍K
    all x <= 0, 近傍K
    左に行ってから折り返してstat: 0 に戻り、最低限の右をとる
        |min left - 0| * 2
        |max right|

    累積和？浮かんだ
    startとの差分浮かんだ
    左と右に分ける

    https://twitter.com/shibh308/status/1033350352454672384
    https://twitter.com/d_tutuz/status/1033357962088075267
    https://twitter.com/satanic0258/status/1033348772758081537
    """
    from bisect import bisect_left
    try:
        # N=7,K=3
        # [-3,-2,-1,0,1,2,3]
        #      |----*---|
        idx = x.index(0)
        left = max(idx - K + 1, 0)
        right = min(idx + 1, N - K)
    except:
        # N=6,K=3
        # [-3,-2,-1,1,2,3]
        #   |-----|*|---|
        idx = bisect_left(x, 0)
        left = max(idx - K, 0)
        right = min(idx + 1, N - K)

    _range = range(left, right + 1)
    # print(idx, _range)
    ans = float("inf")
    for left in _range:
        right = left + K - 1
        # print(left, right)
        # -3,-1,1,2,5,
        # a1:  0->right,right->0,0->left
        # a2:  0->left, left ->0,0->right
        # all posi/nega: 10, 20, 30: to 10, 30-10=20, total=30
        # nega and posi: -10, 20, 30
            # a1: L|-10|=10, |30-(-10)| = 40(10+30), total:50
            # a2: R|+30|=30, |-10-30  | = 40(10+30), total:70
        a1 = abs(x[left]) + abs(x[right] - x[left])
        a2 = abs(x[right]) + abs(x[left] - x[right])
        ans = min([ans, a1, a2])

    return ans


def WA(N, K, x):
    l, r = 0, 0
    for i in range(N-1):
        if x[i] == 0:
            l, r = i, i
            break
        elif x[i+1] == 0:
            l, r = i+1, i+1
            break
        elif x[i] < 0 < x[i+1]:
            l, r = i, i+1
            break

    # WA N=3: 考慮漏れ (ただし、最後のケースでWA N=1)
    if x[-1] < 0:
        l, r = N - 1, N - 1

    ans = float("inf")
    # 左へのルート
    # print((l, r))
    for i in range(l+1):
        t = abs(x[i])
        right = -1
        rem = 0
        fire = abs(i - l) + 1
        if fire == K:
            ans = min(ans, abs(x[i]))
        elif fire > K:
            # out of index
            pass
        else:
            # 右へ向かうのでstartへ戻る
            t *= 2
            rem = K - fire
            right = l + rem
            if right < N:
                ans = min(ans, t + x[right])

        # print(i, l, right, fire, rem, ans, sep="\t")

    # 右へのルート
    # print("----right----")
    for i in range(l, N):
        t = abs(x[i])
        fire = abs(i - r) + 1
        rem = 0
        left = -1
        if fire == K:
            ans = min(ans, abs(x[i]))
        elif fire > K:
            # out of index
            pass
        else:
            # 右へ向かうのでstartへ戻る
            t *= 2
            rem = K - fire
            left = l - rem
            if left >= 0:
                ans = min(ans, t + abs(x[left]))

        # print(left, i, r, fire, rem, ans, sep="\t")

    return ans


if __name__ == '__main__':
    main()
