def main():
    """
    2 <= N <= 3 * 10^5
    |S| = N
    Si = {E, W}
    """
    N = int(input())
    S = input()

    f(N, S)


def f(N, S):
    """
    leaderにする人の東西について
    どちらを向いているか分かればよい
    """
    ans = N
    # 自分を含めて、自分より西にいる人が西を向いている人数
    w_cumsum = [0] * N
    w_cumsum[0] = int(S[0] == "W")
    for i in range(1, N):
        w = int(S[i] == "W")
        w_cumsum[i] = w_cumsum[i-1] + w

    # print(w_cumsum)
    for i in range(N):
        # 対象の外向き
        # 対象より(西and西を向いている人数)+(東and東を向いている人数)
        diff = w_cumsum[i] - int(S[i] == "W")
        diff += (N - (i+1)) - (w_cumsum[-1] - w_cumsum[i])
        ans = min(ans, diff)
        #same = N - 1 - diff
        #print(i, diff, same, ans)

    print(ans)


if __name__ == '__main__':
    main()
