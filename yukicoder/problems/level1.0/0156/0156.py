from itertools import accumulate, takewhile


def main():
    N, M = map(int, input().split())
    C = map(int, input().split())

    ac = accumulate(sorted(C))
    empty_c = takewhile(lambda c: c <= M, ac)
    ans = sum(map(lambda x: 1, empty_c))

    print(ans)

if __name__ == '__main__':
    main()
