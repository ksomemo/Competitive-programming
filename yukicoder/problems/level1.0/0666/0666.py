def main():
    A, B = map(int, input().split())

    m = 1000000007
    ans = (A % m) * (B % m)
    ans %= m
    print(ans)


if __name__ == '__main__':
    main()
