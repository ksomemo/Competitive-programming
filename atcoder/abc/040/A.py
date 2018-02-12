def main():
    n, x = map(int, input().split())

    ans = min(n-x, x-1)
    print(ans)


if __name__ == '__main__':
    main()
