def main():
    A, B, K, L = map(int, input().split())

    x, y = divmod(K, L)
    ans = x * B
    if y > 0:
        ans += min(B, y * A)

    print(ans)


if __name__ == '__main__':
    main()
