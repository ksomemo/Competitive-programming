def main():
    a, b = map(int, input().split())
    if a <= b:
        ans = a
    else:
        ans = a - 1

    print(ans)


if __name__ == '__main__':
    main()
