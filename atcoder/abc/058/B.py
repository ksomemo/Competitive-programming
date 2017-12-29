def main():
    O = input()
    E = input()

    ans = ""
    for o, e in zip(O, E + " "):
        ans += o + e

    print(ans.strip())

if __name__ == '__main__':
    main()
