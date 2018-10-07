def main():
    N, T = map(int, input().split())
    c, t = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    INF = float("inf")
    ans = INF
    for _c, _t in zip(c, t):
        if _t <= T:
            ans = min(ans, _c)

    if ans == INF:
        ans = "TLE"

    print(ans)


if __name__ == '__main__':
    main()
