def main():
    a, b, x = map(int, input().split())

    ans = 0
    if a == 0:
        # 割り切れる
        n_a = 0
        ans += 1
    else:
        # a未満で割り切れるものを除外する
        n_a = (a - 1) // x
    n_b = b // x
    ans += n_b - n_a

    print(ans)

if __name__ == '__main__':
    main()
