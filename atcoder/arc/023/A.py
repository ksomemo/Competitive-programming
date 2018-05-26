def main():
    y = int(input())
    m = int(input())
    d = int(input())

    ans = days(2014, 5, 17) - days(y, m, d)
    print(ans)


def days(y, m, d):
    if m in (1, 2):
        y -= 1
        m += 12

    ans = 365 * y + y // 4 - y // 100 + y // 400
    ans += 306 * (m + 1) // 10 + d - 429

    return ans


if __name__ == '__main__':
    main()
