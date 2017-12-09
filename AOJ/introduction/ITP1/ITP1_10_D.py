def main():
    n = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    dist_ma = sum(abs(x - y) ** 1 for x, y in zip(xs, ys)) ** (1 / 1)
    dist_eu = sum(abs(x - y) ** 2 for x, y in zip(xs, ys)) ** (1 / 2)
    dist_p3 = sum(abs(x - y) ** 3 for x, y in zip(xs, ys)) ** (1 / 3)
    dist_inf = max(abs(x - y) for x, y in zip(xs, ys))

    print(dist_ma)
    print(dist_eu)
    print(dist_p3)
    print(dist_inf)

if __name__ == "__main__":
    main()
