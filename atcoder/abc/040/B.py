def main():
    n = int(input())

    WA_TLE(n)


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
