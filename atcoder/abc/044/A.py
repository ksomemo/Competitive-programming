def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    ans = X * min(K, N) + Y * max(N - K, 0)
    print(ans)


if __name__ == '__main__':
    main()
