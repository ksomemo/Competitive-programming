def main():
    A = int(input())

    ans = AC(A)

    print(ans)


def AC(A):
    ans = -float("inf")
    for y in range(1, A // 2 + 1):
        x = A - y
        xy = x * y
        ans = max(ans, xy)

    return ans


if __name__ == '__main__':
    main()
