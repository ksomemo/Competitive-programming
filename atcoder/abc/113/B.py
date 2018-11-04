def main():
    N = int(input())
    T, A = map(int, input().split())
    *H, = map(int, input().split())

    ts = []
    x = float("inf")
    ans = -1
    for i, h in enumerate(H, 1):
        t = T - h * 0.006
        diff = abs(A - t)
        if diff < x:
            x = diff
            ans = i

    print(ans)


if __name__ == '__main__':
    main()
