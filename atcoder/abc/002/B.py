def main():
    W = input()

    ans = W
    for c in "aiueo":
        ans = ans.replace(c, "")

    print(ans)


if __name__ == '__main__':
    main()
