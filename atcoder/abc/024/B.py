def main():
    N, T = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ans = 0
    for i in range(1, N):
        d = A[i] - A[i - 1]
        if d > T:
            ans += T
        else:
            ans += d
    ans += T

    print(ans)

if __name__ == '__main__':
    main()
