def main():
    N = int(input())
    M = int(input())

    ans = N
    for _ in range(M):
        p, q = map(int, input().split())

        if p == ans:
            ans = q
        elif q == ans:
            ans = p

    print(ans)

if __name__ == '__main__':
    main()
