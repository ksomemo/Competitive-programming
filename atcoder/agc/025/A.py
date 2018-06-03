def main():
    N = int(input())

    ans = f(N)
    print(ans)


def sum_digits(x):
    ans = 0
    while x > 0:
        x, a = divmod(x, 10)
        ans += a
    return ans


def sum_digits_slow(x):
    return sum(map(int, list(str(x))))


def f(N):
    ans = float("inf")
    # 正の整数
    for A in range(1, N//2 + 1):
        B = N - A
        tmp = sum_digits(A) + sum_digits(B)
        ans = min(ans, tmp)

    return ans


if __name__ == '__main__':
    main()
