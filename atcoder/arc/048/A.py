def main():
    A, B = map(int, input().split())

    if 0 < A or B < 0:
        ans = abs(B - A)
    else:
        ans = abs(B - A) - 1

    print(ans)


if __name__ == '__main__':
    main()
