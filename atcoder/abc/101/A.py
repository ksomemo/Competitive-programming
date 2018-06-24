def main():
    S = input()

    ans = 0
    for c in S:
        if c == "+":
            ans += 1
        else:
            ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
