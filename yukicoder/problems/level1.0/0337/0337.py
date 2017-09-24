def main():
    N, P = map(int, input().split())

    # N == 1 or P != 0
    # P == 0
    if P == N * P:
        print("=")
    else:
        print("!=")

if __name__ == '__main__':
    main()
