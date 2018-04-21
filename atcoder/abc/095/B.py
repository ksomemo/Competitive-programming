def main():
    N, X = map(int, input().split())
    M = [
        int(input())
        for _ in range(N)
    ]

    ans = 0
    for i in range(N):
        ans += 1
        X -= M[i]
    ans += X // min(M)

    print(ans)


if __name__ == '__main__':
    main()
