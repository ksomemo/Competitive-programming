def main():
    N = int(input())
    xu = [input().split() for _ in range(N)]

    btc_yen = 380000

    ans = 0
    for x, u in xu:
        if u == "JPY":
            ans += int(x)
        else:
            ans += float(x) * btc_yen

    print(ans)


if __name__ == '__main__':
    main()
