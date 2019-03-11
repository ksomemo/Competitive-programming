def main():
    N = int(input())
    *L, = map(int, input().split())

    s = sorted(L)
    if s[-1] < sum(s[:-1]):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
