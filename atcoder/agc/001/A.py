def main():
    N = int(input())
    *L, = map(int, input().split())

    ans = 0
    L = sorted(L)
    for i in range(0, 2 * N, 2):
        ans += L[i]

    print(ans)

if __name__ == '__main__':
    main()
