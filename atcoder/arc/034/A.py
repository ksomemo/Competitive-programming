def main():
    N = int(input())

    ans = -1
    for _ in range(N):
        a, b, c, d, e = map(int, input().split())
        ans = max(ans, a+b+c+d+(e * 110 / 900))

    print(ans)

if __name__ == '__main__':
    main()
