def main():
    """
    連結: ずれて重なっていてもよい
    """
    W, a, b = map(int, input().split())

    # b <= a <= b + W or a <= b <= a + W:
    # 別の長方形とすでに重なっている
    ans = 0
    if b - (a + W) >= 0:
        # bの左端がaの右側
        ans = b - (a + W)
    elif a - (b + W) >= 0:
        # bの右端がaの左側
        ans = a - (b + W)

    print(ans)


if __name__ == '__main__':
    main()
