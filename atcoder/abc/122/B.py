def main():
    S = input()

    n = len(S)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            x = S[i:j+1]
            tmp = len(x)
            for c in x:
                if c not in "ACGT":
                    tmp = -1
                    break
            ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
