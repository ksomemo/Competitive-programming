def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    f = [False for _ in range(10**5+1)]
    ans = 0
    for a in A:
        if f[a]:
            ans += 1
        f[a] = True

    print(ans)


def editorial(N, A):
    return N - len(set(A))


if __name__ == '__main__':
    main()
