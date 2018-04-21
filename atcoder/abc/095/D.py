def main():
    """
    1 <= N <= 10^5
    2 <= C <= 10^14
    1 <= x1 < x2 < ... < xN < C
    1 <= vi <= 10^9
    """
    N, C = map(int, input().split())
    X, V = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    part_point(N, C, X, V)


def part_point(N, C, X, V):
    ans = 0


if __name__ == '__main__':
    main()
