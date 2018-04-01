from collections import Counter


def main():
    """
    1 ≤ N  ≤ 2 * 10^5
    1 ≤ Di ≤ 10^9
    1 ≤ M  ≤ 2 * 10^5
    1 ≤ Ti ≤ 10^9

    N*M: TLE
    """
    N = int(input())
    D = map(int, input().split())
    M = int(input())
    T = map(int, input().split())

    f(N, D, M, T)


def f(N, D, M, T):
    """
    editorialでは TもCounterに突っ込んでloop数を減らしている
    """
    c = Counter(D)
    for t in T:
        if c[t] == 0:
            print("NO")
            return

        c[t] -= 1

    print("YES")


if __name__ == '__main__':
    main()
