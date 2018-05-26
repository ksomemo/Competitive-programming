def main():
    A, B = map(int, input().split())

    ans = AC(A, B)
    print(ans)


def test_ans():
    _in = [
        (567, 234, 733),
        (999, 100, 899),
        (100, 999, -99),
    ]
    for a, b, ans in _in:
        assert AC(a, b) == f1(a, b) == f2(a, b) == ans


def AC(A, B):
    sa = str(A)
    sb = str(B)

    if sa[0] != "9":
        a = int("9" + sa[1:])
    elif sa[1] != "9":
        a = int(sa[0] + "9" + sa[2])
    else:
        a = int(sa[:2] + "9")

    if sb[0] != "1":
        b = int("1" + sb[1:])
    elif sb[1] != "0":
        b = int(sb[0] + "0" + sb[2])
    else:
        b = int(sb[:2] + "0")

    ans = max(A - b, a - B)
    return ans


def f1(A, B):
    ans = A - B

    sa = str(A)
    sb = str(B)
    for x in range(100, 999+1):
        diff_a = sum(1 for c1, c2 in zip(sa, str(x)) if c1 != c2)
        diff_b = sum(1 for c1, c2 in zip(sb, str(x)) if c1 != c2)
        if diff_a <= 1:
            ans = max(ans, x - B)
        if diff_b <= 1:
            ans = max(ans, A - x)

    return ans


def f2(A, B):
    ans = A - B
    for i in range(3):
        for j in range(9+1):
            if i == 0 and j == 0:
                continue
            a = list(str(A))
            a[i] = str(j)
            a = int("".join(a))
            ans = max(ans, a - B)

    for i in range(3):
        for j in range(9+1):
            if i == 0 and j == 0:
                continue
            b = list(str(B))
            b[i] = str(j)
            b = int("".join(b))
            ans = max(ans, A - b)

    return ans


if __name__ == '__main__':
    main()
