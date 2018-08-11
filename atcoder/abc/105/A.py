def main():
    N, K = map(int, input().split())

    if N % K == 0:
        ans = 0
    else:
        ans = 1

    print(ans)


if __name__ == '__main__':
    main()
