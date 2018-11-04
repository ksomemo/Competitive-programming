def main():
    """
    1 <= N  <= 10^5
    1 <= M  <= 10^5
    0 <= Pi <= N
    0 <= Yi <= 10^9
    Yi != Yj
    """
    N, M = map(int, input().split())
    P, Y = zip(*(
        map(int, input().split())
        for _ in range(M)
    ))

    ans = f(N, M, P, Y)
    print(*ans, sep="\n")


def f(N, M, P, Y):
    piy = [[] for _ in range(N)]
    for i, (p, y) in enumerate(zip(P, Y), 1):
        piy[p-1].append((p, i, y))

    ns = []
    for vs in piy:
        sorted_vs = sorted(vs, key=lambda x: x[2])
        for k, (p, i, _) in enumerate(sorted_vs, 1):
            n = "{:06d}{:06}".format(p, k)
            ns.append((i, n))

    ans = [n for _, n in sorted(ns, key=lambda x: x[0])]

    return ans


if __name__ == '__main__':
    main()
