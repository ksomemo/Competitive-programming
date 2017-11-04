def main():
    """K の正の倍数の 10 進法での各桁の和としてありうる最小の値を求めてください。

    2 ≤ K ≤ 10^5

    min: 1が1つと他が0 -> 10^n, e.g.: 5*2, 25*4
    10倍しても元のKと和は変わらない
    1-9倍とは限らない?: 入力例 2　11111=41×271, 4+1=5では？
    """
    K = int(input())

    ans = sum_digits(K)
    for i in range(2, 10):
        ans = min(ans, sum_digits(K * i))

    print(ans)


def sum_digits(n):
    return sum(map(int, list(str(n))))

if __name__ == '__main__':
    main()
