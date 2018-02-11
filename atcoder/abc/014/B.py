def main():
    n, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if X & (2 ** i):
            ans += A[i]

    print(ans)


if __name__ == '__main__':
    main()
