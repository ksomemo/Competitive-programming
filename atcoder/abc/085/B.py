def main():
    N = int(input())
    D = [int(input()) for _ in range(N)]

    s = set(D)
    ans = len(s)

    print(ans)


if __name__ == '__main__':
    main()
