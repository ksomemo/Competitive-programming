def main():
    n, L, R = map(int, input().split())
    *A, = map(int, input().split())

    ans = [
        min(max(a, L), R)
        for a in A
    ]

    print(*ans)


if __name__ == '__main__':
    main()
