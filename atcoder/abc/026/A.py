def main():
    A = int(input())

    AC(A)


def AC(A):
    ans = -float("inf")
    for y in range(1, A // 2 + 1):
        x = A - y
        xy = x * y
        ans = max(ans, xy)

    print(ans)


def slideshare(A):
    """
    問題文をよく読んでなかった…正の偶数より2で割り切れる
    https://mathtrain.jp/amgm
    a + b >= 2 * math.sqrt(a * b)
    """
    x = A // 2
    ans = x * x
    print(ans)

if __name__ == '__main__':
    main()
