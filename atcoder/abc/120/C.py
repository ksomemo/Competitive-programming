from collections import Counter


def main():
    S = input()

    ans = f(S)
    print(ans)


def f(S):
    """
    A,B,Cそれぞれが存在していたら終了
    存在しない場合
    diff をとる
    """
    b = []
    a = 0
    for c in S:
        if c == '1':
            a += 1
        else:
            a -= 1
        b.append(a)

    ans = 0
    c = Counter(b)
    for k, v in c.items():
        if k == 0:
            ans += v * 2
        else:
            ans += v // 2 * 2

    return ans
    # return WA(b)
    # return WA2(b)


def WA2(b):
    c = Counter([0] + b)
    for _, v in c.items():
        ans += v // 2 * 2
    ans *= 2
    return ans


def WA(b):
    d = [b[0]]
    for a in b[1:]:
        d.append(d[-1] + a)

    print(d)

    c = Counter(b)
    ans = 0
    for v in c.values():
        ans += v // 2
    ans *= 2
    print(c)

    return ans


if __name__ == '__main__':
    main()
