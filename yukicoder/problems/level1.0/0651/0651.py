def main():
    a = int(input())

    # 10の倍数より
    b = int(60 * a / 100)
    h = 10 + b // 60
    m = b % 60

    ans = "{0}:{1:02d}".format(h, m)
    print(ans)


if __name__ == '__main__':
    main()
