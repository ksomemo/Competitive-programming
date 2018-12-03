def main():
    S = input()

    ans = float("inf")
    for i in range(len(S) - 3 + 1):
        x = int(S[i:i+3])
        ans = min(ans, abs(753 - x))

    print(ans)


if __name__ == '__main__':
    main()
