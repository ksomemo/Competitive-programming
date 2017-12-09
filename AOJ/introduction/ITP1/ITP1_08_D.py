def main():
    s = input()
    p = input()

    # |p| <= |s| より
    if p in s + s:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
