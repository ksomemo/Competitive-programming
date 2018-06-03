def main():
    N, A = map(int, input().split())
    *X, = map(int, input().split())

    ans = part(N, A, X)
    print(ans)


def f(N, A, X):
    ans = 0
    print(ans)


def part(N, A, X):
    import sys
    sys.setrecursionlimit(10 ** 7)
    a = [0] * N

    def rec(i, n):
        ans = 0
        if i == n:
            s = 0
            c = 0
            #print(a)
            for j, b in enumerate(a):
                if b == 1:
                    s += X[j]
                    c += 1

            if c == 0:
                return 0
            if s / c == A:
                return 1
            else:
                return 0

        a[i] = 0
        ans += rec(i + 1, n)
        a[i] = 1
        ans += rec(i + 1, n)

        return ans

    ans = rec(0, N)
    return ans


if __name__ == '__main__':
    main()
