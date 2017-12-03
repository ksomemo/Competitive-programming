def main():
    N, C = map(int, input().split())
    x = [
        [int(x) for x in input().split()]
        for _ in range(N)
    ]

    # 被っている時間をどうするか
    for s, t, c in x:
        s - 0.5, t, c

if __name__ == '__main__':
    main()
