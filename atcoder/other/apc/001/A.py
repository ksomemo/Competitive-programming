def main():
    X, Y = map(int, input().split())
    # a = n * X
    # x = m * Y: NG
    # a % Y = 0: NG
    if X % Y == 0:
        print(-1)
        return

    ans = X * (Y - 1)
    print(ans)


if __name__ == '__main__':
    main()
