def main():
    A, B, X = map(int, input().split())

    if A > X:
        print("NO")
    elif A + B >= X:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
