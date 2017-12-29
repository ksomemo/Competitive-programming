def main():
    N, M = map(int, input().split())
    pos = [
        list(map(int, input().split()))
        for i in range(N)
    ]
    checkpoints = [
        list(map(int, input().split()))
        for i in range(M)
    ]

    for x1, y1 in pos:
        ans = 0
        min_m = float("inf")
        for i, (x2, y2) in enumerate(checkpoints, 1):
            m = abs(x1 - x2) + abs(y1 - y2)
            if min_m > m:
                ans = i
                min_m = m

        print(ans)

if __name__ == '__main__':
    main()
