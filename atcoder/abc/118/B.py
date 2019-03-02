def main():
    N, M = map(int, input().split())

    x = [[0] * N for _ in range(M)]
    for i in range(N):
        K, *A, = map(int, input().split())
        for a in A:
            x[a-1][i] = 1

    ans = 0
    for y in x:
        if sum(y) == N:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
