def main():
    A, B = map(int, input().split())

    ab = A * B
    if ab % 2 == 0:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
