def main():
    """
      1-  9
     11- 99
    111-999
    ...
    """
    N = int(input())

    ans = AC(N)
    print(ans)


def test_ans():
    a, e1, e2 = [], [], []
    for i in range(1, 50+1):
        a.append(AC(i))
        e1.append(editorial1(i))
        e2.append(editorial2(i))

    assert a == e1
    assert a == list(map(str, e2))


def AC(N):
    z = []
    a = 0
    b = 1
    for i in range(N):
        a += 1
        if a % 10 == 0:
            a = 1
            b += 1

        z.append(str(a) * b)

    ans = z[-1]
    return ans


def editorial1(N):
    a, b = divmod(N - 1, 9)
    return str(b + 1) * (a + 1)


def editorial2(N):
    """
     99999 (5桁目*9)
    111111-555555 (N=50)
    """
    z = []
    for i in range(1, 555555+1):
        if len(set(str(i))) == 1:
            z.append(i)

    return z[N-1]


if __name__ == '__main__':
    main()
