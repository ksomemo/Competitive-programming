def main():
    """
    1 <= x <= 10**15

    どのパターンで得点が一番多いか
    (5) -> 6 -> 5 > 6 -> 5 ...
    """
    x = int(input())

    d1, r1 = divmod(x, 11)
    ans = d1 * 2 + (r1 // 6) + (r1 % 6 > 0)

    print(ans)

if __name__ == '__main__':
    main()
