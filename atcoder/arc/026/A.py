def main():
    N, A, B = map(int, input().split())

    g = min(N, 5)
    ans = (N - g) * A + g * B
    print(ans)


if __name__ == '__main__':
    main()
