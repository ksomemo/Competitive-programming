def main():
    s = input()

    ans = AC(s)
    if ans:
        print("YES")
    else:
        print("NO")


def test_ans():
    for s in ("ab*", "abc", "a*bc*", "***"):
        assert AC(s) == editorial(s)


def AC(s):
    n = len(s)
    for i in range(n // 2):
        c = s[n - i - 1]
        if s[i] == "*" or c == "*" or s[i] == c:
            continue
        return False

    return True


def editorial(s):
    s2 = s[::-1]
    for c1, c2 in zip(s, s2):
        if c1 == "*" or c2 == "*" or c1 == c2:
            continue
        return False

    return True


if __name__ == '__main__':
    main()
