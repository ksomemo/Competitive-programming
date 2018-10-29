def main():
    N, M, A, B = map(int, input().split())
    L, R = zip(*[
        map(int, input().split())
        for _ in range(M)
    ])

    a = [False] * N
    for l, r in zip(L, R):
        for i in range(l, r + 1):
            a[i-1] = True

    ans = 0
    for is_a in a:
        ans += A if is_a else B

    print(ans)


if __name__ == '__main__':
    main()
