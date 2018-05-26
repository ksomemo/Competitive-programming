def main():
    N = int(input())
    ab = [
        map(int, input().split())
        for _ in range(N)
    ]

    s = 0
    for a, b in ab:
        s += a*b
        # print(a,b,a*b)

    ans = int(s*1.05)
    print(ans)


if __name__ == '__main__':
    main()
