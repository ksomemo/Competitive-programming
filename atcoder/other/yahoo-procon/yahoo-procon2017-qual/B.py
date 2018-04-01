def main():
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    A = sorted(A)
    ans = 0
    for i in range(K):
        ans += A[i] + i

    print(ans)


if __name__ == '__main__':
    main()
