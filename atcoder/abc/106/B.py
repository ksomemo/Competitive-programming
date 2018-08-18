def main():
    N = int(input())

    ans = f(N)
    print(ans)


def f(N):
    ans = 0
    for i in range(1, N+1, 2):
        x = 0
        for j in range(1, i+1, 2):
            if i % j == 0:
                x += 1

        if x == 8:
            ans += 1

    return ans


if __name__ == '__main__':
    main()
