def main():
    n = int(input())

    if n % 2 == 0:
        ans = n - 1
    else:
        ans = n + 1
    print(ans)


if __name__ == '__main__':
    main()
