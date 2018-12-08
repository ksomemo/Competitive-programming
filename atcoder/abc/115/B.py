def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]

    ans = sum(p) - max(p) // 2
    print(ans)


if __name__ == '__main__':
    main()
