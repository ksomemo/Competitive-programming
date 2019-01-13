def main():
    """
    問題が 3問出題され、
    1問目の配点は A点以下、
    2問目の配点は A+1点以上 B点以下、
    3問目の配点は  B+1点以上である。
    """
    S = input()
    ans = f(S)
    if ans:
        print("YES")
    else:
        print("NO")


def f(S):
    n = len(S)
    ok = False
    target = "keyence"
    for i in range(n):
        for j in range(i, n):
            # print(S[:i], S[i:j], S[j:])
            if S[:i] == target:
                return True
            elif S[:i] + S[j:] == target:
                return True
            elif S[j:] == target:
                return True

    return False


if __name__ == '__main__':
    main()
