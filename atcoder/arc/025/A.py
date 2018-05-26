def main():
    D = map(int, input().split())
    J = map(int, input().split())

    editorial(D, J)


def AC(D, J):
    ans = 0
    for d, j in zip(D, J):
        ans += max(d, j)

    print(ans)


def editorial(D, J):
    D = list(D)
    J = list(J)

    ans = 0
    for i in range(2 ** 7):
        tmp = 0
        for j in range(7):
            if i >> j & 1:
                tmp += D[j]
            else:
                tmp += J[j]
        ans = max(ans, tmp)

    print(ans)


if __name__ == '__main__':
    main()
