def main():
    s = input()

    ans = ""
    for c in s:
        if c in ("0", "1"):
            ans += c
        else:
            ans = ans[:-1]
    print(ans)


if __name__ == '__main__':
    main()
