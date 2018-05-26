def main():
    N, K = map(int, input().split())
    t = [int(input()) for _ in range(N)]

    for i in range(2, N):
        s = sum(t[i-2:i+1])
        if s < K:
            print(i + 1)
            return

    print(-1)


if __name__ == '__main__':
    main()
