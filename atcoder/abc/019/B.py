def main():
    s = input()

    ans = ""
    bef = s[0]
    for c in s[1:]:
        if bef[0] == c:
            bef += c
        else:
            ans += bef[0] + str(len(bef))
            bef = c

    ans += bef[0] + str(len(bef))

    print(ans)


def f(s):
    """https://beta.atcoder.jp/contests/abc019/submissions/1240782

    下記と同じような挙動
    https://docs.python.jp/3/library/itertools.html#itertools.groupby
    """
    import re
    ans = ""
    # キャプション
    for g, k in re.findall(r"((.)\2*)", s):
        ans += k + str(len(g))

    return ans

if __name__ == '__main__':
    main()
