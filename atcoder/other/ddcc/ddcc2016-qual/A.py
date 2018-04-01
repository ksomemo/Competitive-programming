def main():
    A, B, C = map(int, input().split())

    # A: C = B: X
    X = C * B / A

    print(X)


if __name__ == '__main__':
    main()
