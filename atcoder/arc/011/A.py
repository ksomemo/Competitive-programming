def main():
    m, n, N = map(int, input().split())

    ans = N
    small = N
    while small >= m:
        n_m = small // m
        rem = small % m
        new_pen = n_m * n
        ans += new_pen
        small = new_pen + rem

    print(ans)


if __name__ == '__main__':
    main()
