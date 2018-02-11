from collections import Counter


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    f(A)


def AC(A):
    c = Counter(A)
    ans = sorted(c.keys())[-2]

    print(ans)


def f(A):
    s = set(A)
    ans = sorted(list(s))[-2]
    print(ans)

if __name__ == '__main__':
    main()
