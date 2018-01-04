def main():
    """
    |s| <= 2 * 10 ** 5
    """
    s = input()

    for i, c in enumerate(s):
        if c == "A":
            start = i
            break

    for i, c in enumerate(s[start + 1:], start + 1):
        if c == "Z":
            end = i

    ans = end - start + 1
    print(ans)

if __name__ == '__main__':
    main()
