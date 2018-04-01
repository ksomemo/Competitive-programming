def main():
    N = int(input())
    A = map(int, input().split())

    d = {}
    ans = 0
    for i, a in enumerate(A, 1):
        x, y = min(i, a), max(i, a)
        d[(x, y)] = d.get((x, y), 0) + 1
        if d[(x, y)] == 2:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
