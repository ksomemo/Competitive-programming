def main():
    S = input()

    s = set(S)
    if s == set("NWSE") or s == set("NS") or s == set("WE"):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
