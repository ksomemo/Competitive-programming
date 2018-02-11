def main():
    S = input()
    N = int(input())

    LR = [
        tuple(map(int, input().split()))
        for _ in range(N)
    ]

    for l, r in LR:
        s1 = S[:l - 1]
        s2 = "".join(reversed(S[l - 1:r]))
        s3 = S[r:]
        S = s1 + s2 + s3

    print(S)

if __name__ == '__main__':
    main()
