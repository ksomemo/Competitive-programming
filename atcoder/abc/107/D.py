def main():
    """
    """
    N = int(input())
    *a, = map(int, input().split())

    ans = editorial(N, a)
    ans = TLE(N, a)
    print(ans)


def editorial(N, a):
    """
    """
    ans = 0
    return ans


def TLE(N, a):
    ms = []
    for l in range(N):
        for r in range(l, N):
            seq = a[l:r+1]
            idx = len(seq) // 2
            m = sorted(seq)[idx]
            # print(seq, m)
            ms.append(m)

    ans = sorted(ms)[len(ms) // 2]
    return ans


if __name__ == '__main__':
    main()
