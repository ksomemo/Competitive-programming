def main():
    N, M, C = map(int, input().split())
    *B, = map(int, input().split())
    A = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ans = 0
    for pa in A:
        x = sum(a*b for a, b in zip(pa, B)) + C
        ans += x > 0

    print(ans)


if __name__ == '__main__':
    main()
