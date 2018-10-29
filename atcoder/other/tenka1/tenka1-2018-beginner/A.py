def main():
    S = input()

    if len(S) == 2:
        print(S)
    else:
        print(S[::-1])


if __name__ == '__main__':
    main()
