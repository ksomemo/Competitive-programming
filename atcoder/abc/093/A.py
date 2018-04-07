def main():
    S = input()

    if sorted(S) == list("abc"):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
