def main():
    C, c = input().split()

    diff = ord("a") - ord("A")
    ans = ord(C) == ord(c) - diff
    # ans = C.lower() == c
    if ans:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
