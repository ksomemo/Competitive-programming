from collections import Counter


def main():
    N, K = map(int, input().split())
    A = map(int, input().split())

    c = Counter(A)

    ans = 0
    n_type = len(c)
    for count in sorted(c.values()):
        if n_type <= K:
            break
        ans += count
        n_type -= 1

    print(ans)

if __name__ == '__main__':
    main()
