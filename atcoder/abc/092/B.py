def main():
    N = int(input())
    D,X = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    ans = X
    for i in range(N):
        for j in range(1, D+1, A[i]):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
