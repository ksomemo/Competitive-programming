def main():
    A, B = map(int, input().split())

    if A * 2 > 16 or B * 2 > 16:
        print(":(")
    else:
        print("Yay!")


if __name__ == '__main__':
    main()
