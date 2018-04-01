def main():
    """
    1 <= N <= 100
    -100 <= ai <= 100
    """
    N = int(input())
    *A, = map(int, input().split())

    ans = float("inf")
    for to in range(-100, 100 + 1):
        cost = 0
        for a in A:
            cost += (a - to) ** 2
        ans = min(ans, cost)

    print(ans)


if __name__ == '__main__':
    main()
