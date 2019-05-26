def main():
    A, B = map(int, input().split())

    if A <= 5:
        ans = 0
    elif A <= 12:
        ans = B // 2
    else:
        ans = B
    print(ans)


if __name__ == '__main__':
    main()
