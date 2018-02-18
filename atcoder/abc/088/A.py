def main():
    N = int(input())
    A = int(input())

    m = N % 500
    if m == 0:
        print("Yes")
        return

    if m <= A:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
