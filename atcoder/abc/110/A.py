def main():
    A, B, C = map(int, input().split())

    ans = AC(A, B, C)
    assert ans == AC2(A, B, C)
    print(ans)


def AC2(A, B, C):
    ns = [A, B, C]
    ans = sum(ns) + max(ns) * 9
    return ans


def AC(A, B, C):
    n = sorted([A, B, C])
    ans = n[0] + n[1] + n[2] * 10
    return ans


if __name__ == '__main__':
    main()
