def main():
    n = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for a in A:
        ans += a - f(a)

    print(ans)


def f(a):
    for i in range(a, -1, -1):
        # p1
        if i % 2 == 0:
            continue
        # p2
        if i % 3 == 2:
            continue

        return i

if __name__ == '__main__':
    main()
