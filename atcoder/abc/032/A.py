def main():
    a = int(input())
    b = int(input())
    n = int(input())

    AC(a, b, n)
    # naive_AC(a, b, n)


def AC(a, b, n):
    def gcd(a, b):
        if a < b:
            return gcd(b, a)

        c = a % b
        if c == 0:
            return b
        return gcd(b, c)

    def lcm(a, b):
        return a * b // gcd(a, b)

    # どちらでも割り切れる数
    l = lcm(a, b)
    # 割り切れればn, 割り切れなければ倍数に調整
    m = n % l
    ans = n - m
    if m != 0:
        ans += l
    print(ans)


def naive_AC(a, b, n):
    for i in range(n, n*n):
        if i % a == 0 and i % b == 0:
            print(i)
            break


if __name__ == '__main__':
    main()
