def main():
    N = int(input())
    m = map(int, input().split())

    ans = 0
    for x in m:
        # ACだけど、素直に書くべき
        # ans += max(80 - x, 0))
        ans += abs(min(x - 80, 0))

    print(ans)


if __name__ == '__main__':
    main()
