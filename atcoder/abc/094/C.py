def main():
    """
    N=2*10^5
    毎回sortは無理
    sort済みにして計算量を落とす

    元が偶数個なので中央値を考えてsortしたとき
    中央付近には2つ,sort済み値が存在する m1<=m2
    1つ除外したとき
        除外したものがm1以下: 小さい方にずれるのでm2
        除外したものがm2以上: 大きい方にずれるのでm1
    """
    N = int(input())
    *X, = map(int, input().split())

    X_sorted = sorted(X)
    mid = N // 2
    m1 = X_sorted[mid-1]
    m2 = X_sorted[mid]
    for i in range(N):
        if X[i] <= m1:
            ans = m2
        else:
            ans = m1

        print(ans)


if __name__ == '__main__':
    main()
