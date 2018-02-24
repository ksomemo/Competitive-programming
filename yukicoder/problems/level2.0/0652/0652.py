def main():
    a, b, S = input().split()

    a, b = int(a), int(b)
    S = S.replace("UTC", "")

    # UTC
    sign = (-1, 1)[S[0] == "+"]
    x = S[1:].split(".")
    x1, x2 = int(x[0]), 0
    if len(x) > 1:
        x2 = int(x[1])

    # 小数点以下、minutesの調整
    b2 = b + sign * x2 * 6
    m = b2 % 60

    # hourの調整
    h_sub = b2 // 60
    x1_2 = sign * x1 - 9
    h = (a + h_sub + x1_2) % 24

    ans = "{:02d}:{:02d}".format(h, m)

    print(ans)


if __name__ == '__main__':
    main()
