def main():
    """
    連結: グラフ上の任意の2頂点間にpathが存在する(ノード1でもよい)

    1-2-3-4-5-6
    └---------┘
        1つ頂点を削除すると1つ
            1-2-3-4-5
        2つ頂点を削除すると最大2つ
            1   3-4-5
        3つ頂点を削除すると最大3つ
            1   3   5
    """
    n = int(input())
    k = int(input())

    editorial(n, k)


def editorial(n, k):
    x = n - 1
    # 切り上げ
    if k <= (x + 2 - 1) // 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
