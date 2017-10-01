def main():
    S = input()
    trans = {
        ">": "<",
        "<": ">"
    }
    rev = reversed(S)
    ans = "".join(map(lambda s: trans[s], rev))
    print(ans)

if __name__ == '__main__':
    main()
