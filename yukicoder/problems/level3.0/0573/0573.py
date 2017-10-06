def main():
    N = int(input())

    # 0 to N - 1
    # a[a[i]] = a[i]

    # all same, どれを選んでも同じになる
    # all: index eq value, それぞれが同じ値をとる
    # N番目の数値が、あるindexを示す場合
    # そのindexの場所の値はindexと同じであること

    n_comb = 0
    print(n_comb % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
