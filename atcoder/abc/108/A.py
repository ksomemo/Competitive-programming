def main():
    K = int(input())

    ans = editorial(K)
    assert ans == AC(K) == loop(K)
    print(ans)


def editorial(K):
    """
    K % 2 == 0: 奇数も偶数も同じ個数、K+1//2しても結果は変わらない 
    K % 2 == 1: 奇数のほうが多い、Kは奇数なのでK//2では繰り下がりK+1//2は繰り上がる
    """
    return (K // 2) * ((K + 1) // 2)


def loop(K):
    """
    (K // 2) * (K - K // 2)
    """
    even = sum(1 for i in range(1, K+1) if i % 2 == 0)
    return even * (K - even)


def AC(K):
    d = {}
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            p = tuple(sorted((i, j)))
            if i % 2 == 1 and j % 2 == 0:
                d[p] = 1
            elif i % 2 == 0 and j % 2 == 1:
                d[p] = 1

    ans = len(d)
    return ans


if __name__ == '__main__':
    main()
