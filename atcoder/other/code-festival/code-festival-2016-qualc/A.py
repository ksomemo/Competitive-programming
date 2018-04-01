def main():
    S = input()

    if "C" not in S:
        print("No")
        return

    c_idx = S.index("C")
    if "F" not in S[c_idx + 1:]:
        print("No")
        return

    print("Yes")


if __name__ == '__main__':
    main()
