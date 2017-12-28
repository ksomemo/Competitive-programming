def main():
    N, T = map(int, input().split())
    ts = list(map(int, input().split()))

    ans = 0
    for i in range(N - 1):
        t1 = ts[i]
        t2 = ts[i + 1]
        ans += min(t2 - t1, T)
    ans += T

    print(ans)

if __name__ == '__main__':
    main()
