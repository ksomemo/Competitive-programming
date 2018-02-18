def main():
    N = int(input())
    A = map(int, input().split())

    A = sorted(A, reverse=True)
    alice, bob = 0, 0
    for i, a in enumerate(A):
        if i % 2 == 0:
            alice += a
        else:
            bob += a

    ans = alice - bob
    print(ans)


if __name__ == '__main__':
    main()
