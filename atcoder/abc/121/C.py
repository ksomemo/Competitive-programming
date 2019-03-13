def main():
    N, M = map(int, input().split())
    ab = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ab = sorted(ab, key=lambda x: x[0])
    d = 0
    ans = 0
    for a, b in ab:
        if d + b <= M:
            ans += a * b
            d += b
        else:
            ans += (M-d) * a
            break

    print(ans)


if __name__ == '__main__':
    main()
