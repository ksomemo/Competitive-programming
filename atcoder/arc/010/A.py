def main():
    N, M, A, B = map(int, input().split())
    cs = [int(input()) for _ in range(M)]

    for d, c in enumerate(cs, 1):
        if N <= A:
            N += B
        if N < c:
            print(d)
            return

        N -= c

    print("complete")


if __name__ == '__main__':
    main()
