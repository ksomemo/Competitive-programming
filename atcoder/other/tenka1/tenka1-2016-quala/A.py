def main():
    # solve(10)
    solve(100)


def solve(N):
    ans = 0
    for i in range(1, N + 1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i

    print(ans)


if __name__ == '__main__':
    main()
