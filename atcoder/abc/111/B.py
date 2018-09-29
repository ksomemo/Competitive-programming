def main():
    N = int(input())

    ans1 = AC1(N)
    ans2 = AC2(N)
    assert ans1 == ans2

    print(ans1)


def AC1(N):
    for i in range(N, 999+1):
        if len(set(list(str(i)))) == 1:
            return i


def AC2(N):
    for i in range(1, 9+1):
        if N <= 111 * i:
            return 111 * i


if __name__ == '__main__':
    main()
