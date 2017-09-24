def main():
    N = int(input())

    total_b = 0
    b = 1
    ans = 0
    while True:
        if total_b + b == N:
            break

        if total_b + b * 2 > N:
            # N = (X - Y) + 2 * Y
            # N = X + Y
            next_b = N - (total_b + b)
            total_b = b - next_b
            b = next_b
            continue
        ans += 1
        b *= 2

    print(ans)
if __name__ == '__main__':
    main()
