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
    ans = WA(N, K, x)
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
    """
    ans = float("inf")

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
