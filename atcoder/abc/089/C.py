from itertools import combinations


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    f(S)


def f(S):
    march = list("MARCH")
    n = {k: 0 for k in march}
    for s in S:
        if s[0] in march:
            n[s[0]] += 1

    ans = 0
    for a, b, c in combinations(march, 3):
        ans += n[a] * n[b] * n[c]

    print(ans)


if __name__ == '__main__':
    main()
