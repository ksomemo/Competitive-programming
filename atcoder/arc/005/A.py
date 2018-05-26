def main():
    N = int(input())
    s = input()

    ans = 0
    ws = s[:-1].split()
    for w in ws:
        if w in ("TAKAHASHIKUN", "Takahashikun", "takahashikun"):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
