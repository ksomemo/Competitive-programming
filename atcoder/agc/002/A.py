def main():
    a, b = map(int, input().split())

    if a <= 0 <= b:
        ans = "Zero"
    elif a > 0:
        ans = "Positive"
    elif b < 0:
        ans = "Negative"
        c = b - a
        # a == bのとき負が2個
        # (ACになった,解説はCの偶奇性を見ているのでA=BのときはAのみ？)
        # if c == 0 or c % 2 == 1:
        if c % 2 == 1:
            ans = "Positive"

    print(ans)


if __name__ == '__main__':
    main()
