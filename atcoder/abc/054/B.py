def main():
    N, M = map(int, input().split())
    A = [
        input()
        for i in range(N)
    ]
    B = [
        input()
        for i in range(M)
    ]

    diff = N - M + 1
    for i in range(diff):
        for j in range(diff):
            a = [
                A[k][j:j + M]
                for k in range(i, i + M)
            ]
            if a == B:
                print("Yes")
                return

    print("No")

if __name__ == '__main__':
    main()
