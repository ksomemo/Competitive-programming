from collections import Counter


def main():
    """
    blue: a, a, d
    red:  a, b, c

    a: 2-1= 1
    b,c: 0-1=-1
    d: 1-0=1
    """
    N = int(input())
    S = [input() for _ in range(N)]
    M = int(input())
    T = [input() for _ in range(M)]

    b = Counter(S)
    r = Counter(T)
    b_r = b - r

    ans = 0
    for word, count in b_r.most_common():
        ans = max(ans, count)
        break

    print(ans)


if __name__ == '__main__':
    main()
