def main():
    X = input()

    ans = part(X)
    print(ans)


def part(X):
    while True:
        n = len(X)
        for i in range(n-1):
            if X[i:i+2] == "ST":
                X = X[:i] + X[i+2:]
                break

        if n == len(X):
            break

    return len(X)


if __name__ == '__main__':
    main()
