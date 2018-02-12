def main():
    n, m = map(int, input().split())

    h = n % 12
    hm = (360 // 12) * (m / 60)
    hd = (360 // 12) * h + hm
    md = (360 // 60) * m
    ans = abs(hd - md)
    # なす角 180以下
    if ans > 180:
        ans = 360 - ans

    print(ans)


if __name__ == '__main__':
    main()
