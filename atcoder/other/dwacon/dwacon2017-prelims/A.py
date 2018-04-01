def main():
    n, a, b = map(int, input().split())

    d = n - a - b
    if d >= 0:
        ans = 0
    else:
        ans = abs(d)

    print(ans)


if __name__ == '__main__':
    main()
