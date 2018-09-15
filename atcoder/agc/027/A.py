def main():
    """
    2 <= N <= 100
    1 <= ai,x <= 10^9
    """
    N, x = map(int, input().split())
    *a, = map(int, input().split())

    ans = 0
    # 喜ぶようにちょうど配る
    for _a in sorted(a):
        if _a <= x:
            ans += 1
            x -= _a

    # ちょうど配るには多かった
    # ans < N であれば、喜んでいないだれかに押し付ける
    if x > 0 and ans == N:
        ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
