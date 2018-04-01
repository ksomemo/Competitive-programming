def main():
    S = input()

    right = "CODEFESTIVAL2016"
    ans = sum(c1 != c2 for c1, c2 in zip(S, right))
    print(ans)


if __name__ == '__main__':
    main()
