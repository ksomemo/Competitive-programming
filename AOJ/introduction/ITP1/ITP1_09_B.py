def main():
    while True:
        S = input()
        if S == "-":
            break

        n_shuffle = int(input())
        hs = [int(input()) for _ in range(n_shuffle)]

        for h in hs:
            S = S[h:] + S[:h]

        print(S)

if __name__ == "__main__":
    main()
