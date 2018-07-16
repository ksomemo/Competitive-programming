def main():
    """
    2 <= N <= 100
    1 <= ai <= N

    色の種類は10^4存在するが、N<=100より色は気にしなくて良い
    もし2色なら奥の色を考慮する必要がある

    abab: 0
    aaab: 1 (abab)
    aabb: 2 (acbc)
    aaaa: 2 (acac)
        2つ目のaを変更したあと、2と3つ目の関係を気にする必要がないので4つ目を考える
        4つ目を考慮することで3/5との関係を考慮できる
    """
    N = int(input())
    *A, = map(int, input().split())

    # A.append(-1)
    ans = 0
    i = 1
    while i < N:
        if A[i-1] == A[i]:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)


if __name__ == '__main__':
    main()
