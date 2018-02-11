def main():
    N = int(input())

    # 4 - 100: intにできる結果しかない
    s = sum(range(1, N+1)) * 10000
    ans = s // N
    print(ans)


def f(N):
    """mainのintの理由

    下記等差数列の和をNで割れば良い
    N * (a1 + an) / 2
    金額は10,000円単位なので
    Nが1増えるごとに1/2*10000=5000ずつ増える
    """
    return 10000 * (1 + N) // 2


if __name__ == '__main__':
    main()
