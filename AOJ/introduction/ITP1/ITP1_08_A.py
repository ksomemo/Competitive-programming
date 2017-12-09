def main():
    S = input()
    # my swapcase
    for s in S:
        o = ord(s)
        if 97 <= o < 97 + 26:
            o -= 32
        elif 65 <= o < 65 + 26:
            o += 32

        print(chr(o), end="")
    print("")

if __name__ == "__main__":
    main()
