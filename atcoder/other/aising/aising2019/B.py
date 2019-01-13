def main():
    """
    問題が 3問出題され、
    1問目の配点は A点以下、
    2問目の配点は A+1点以上 B点以下、
    3問目の配点は  B+1点以上である。
    """
    N = int(input())
    A, B = map(int, input().split())
    *P, = map(int, input().split())

    n_a = 0
    n_ab = 0
    n_b = 0
    for p in P:
        if p > B:
            n_b += 1
        elif A < p <= B:
            n_ab += 1
        elif p <= A:
            n_a += 1

    ans = min([n_a, n_ab, n_b])
    print(ans)


if __name__ == '__main__':
    main()
