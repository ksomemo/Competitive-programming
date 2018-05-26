def main():
    A, K = map(int, input().split())

    TRI_2 = 2 * 10 ** 12
    if K == 0:
        # A:0, K:0 -> N=TRI_2 -> TLE
        ans = TRI_2 - A
    else:
        # A:0, K:1 -> 1,3,7,15 (約二倍ずつ, log)
        t = A
        ans = 0
        while t < TRI_2:
            t += 1 + K * t
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
