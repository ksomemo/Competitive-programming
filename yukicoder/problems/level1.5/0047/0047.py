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


def main2():
    # 10^8 100000000
    # 2^26 67108864
    # 2^27 134217728
    N = int(input())

    for p in range(27):
        if N <= 2 ** p:
            print(p)
            return

    print(27)

if __name__ == '__main__':
    main2()
