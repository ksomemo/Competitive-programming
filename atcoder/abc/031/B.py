def main():
    L, H = map(int, input().split())
    N = int(input())
    A = [int(input()) for _ in range(N)]

    for a in A:
        if L <= a <= H:
            print(0)
        elif a > H:
            print(-1)
        else:
            print(L-a)


if __name__ == '__main__':
    main()
