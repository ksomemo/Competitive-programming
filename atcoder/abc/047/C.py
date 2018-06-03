def main():
    S = input()

    b = sum(1 for x in S.split("W") if x.startswith("B"))
    w = sum(1 for x in S.split("B") if x.startswith("W"))
    ans = b + w - 1

    print(ans)


def test_editorial():
    def n_period(S):
        bef = ""
        ans = 0
        for c in S:
            if bef != c:
                ans += 1
            bef = c
        return ans

    assert n_period("W") == 1
    assert n_period("WB") == 2
    assert n_period("BWWBBWBB") == 5


if __name__ == '__main__':
    main()
