def main():
    A, B = map(int, input().split())

    a = abs(A)
    b = abs(B)
    if a < b:
        print("Ant")
    elif a > b:
        print("Bug")
    else:
        print("Draw")


if __name__ == '__main__':
    main()
