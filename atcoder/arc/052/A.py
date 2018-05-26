def main():
    S = input()

    nums = list("0123456789")
    ans = ""
    for c in S:
        if c in nums:
            ans += c

    print(ans)


if __name__ == '__main__':
    main()
