def main():
    w = input()

    for o in range(ord('a'), ord('z')+1):
        c = chr(o)
        if w.count(c) % 2 == 1:
            print("No")
            return

    print("Yes")


if __name__ == '__main__':
    main()
