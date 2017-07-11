def main():
    s = input().strip()
    if len(s) == len(set(s)):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
