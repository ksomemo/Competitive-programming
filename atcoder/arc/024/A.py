def main():
    L, R = map(int, input().split())

    ls = map(int, input().split())
    rs = map(int, input().split())

    f(ls, rs)


def f(ls, rs):
    ln = [0] * 41
    rn = [0] * 41
    for l in ls:
        ln[l] += 1
    for r in rs:
        rn[r] += 1

    ans = 0
    for n1, n2 in zip(ln[10:], rn[10:]):
        n = min(n1, n2)
        ans += n

    print(ans)


def WA(ls, rs):
    """左右気にせず2足ずつにしてしまった
    """
    from collections import Counter
    lc = Counter(ls)
    rc = Counter(rs)
    ans = 0
    for size, n in (lc + rc).items():
        ans += n//2

    print(ans)


if __name__ == '__main__':
    main()
