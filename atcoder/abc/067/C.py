def main():
    """
    1.
        |前半合計 - 後半合計|
    ↓
    2.
        全体合計 = 前半合計 + 後半合計
        |全体合計 - 前半合計 * 2|
        |後半合計 - 前半合計|
        => 1.

    [計算量]
    1.
    N-loop:
        sum - sum => O(N)

    2.
    1-loop: sum => O(N)
    N-loop:
        add
        sum(計算済み) - cumsum * 2
        => O(1)
    """
    N = int(input().strip())
    a = list(map(int, input().strip().split()))
    s = sum(a)
    min_v = float("inf")
    cumsum = 0
    for i in range(N):
        cumsum += a[i]
        if i >= 1:
            min_v = min(min_v, abs(s - 2 * cumsum))

    print(min_v)

if __name__ == '__main__':
    main()
