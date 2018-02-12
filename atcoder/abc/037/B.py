def main():
    N, Q = map(int, input().split())
    lrt = [
        map(int, input().split())
        for _ in range(Q)
    ]

    A = [0 for _ in range(N)]
    for l, r, t in lrt:
        l, r = l-1, r-1
        for i in range(l, r+1):
            A[i] = t

    for a in A:
        print(a)


if __name__ == '__main__':
    main()
