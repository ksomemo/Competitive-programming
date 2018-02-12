def main():
    n = int(input())

    # WA_TLE(n)
    AC(n)


def AC(n):
    import math

    ans = float("inf")
    x = math.floor(math.sqrt(n))
    for w in range(1, x + 1):
        # 長方形として成立するh
        h = n // w
        tmp = n - w * h + abs(w - h)
        ans = min(ans, tmp)

    print(ans)


def WA_TLE(n):
    ans = float("inf")
    for x in range(1, n):
        for y in range(1, n-x+1):
            s = x * y
            r = n - s
            if r < 0:
                continue
            ans = min(ans, r + abs(x-y))

    print(ans)


if __name__ == '__main__':
    main()
