from collections import Counter, OrderedDict


def main():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]

    c = Counter(A)

    order_no = []
    for i in range(1, N+1):
        if i not in c:
            order_no.append(i)

    order_yes = OrderedDict()
    for a in reversed(A):
        if a not in order_yes:
            order_yes[a] = None

    for i in order_yes.keys():
        print(i)
    for i in order_no:
        print(i)


if __name__ == '__main__':
    main()
