def main():
    S = input()

    if S[-2:] == "ai":
        print(S[:-2] + S[-2:].upper())
    else:
        print(S + "-AI")

if __name__ == '__main__':
    main()
