def main():
    n = int(input())
    ans = solve1(n)
    print(ans)


def solve1(n):
    if n <= 1:
        return 1
    a, b = 1, 1

    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    main()
