def main():
    N = int(input())
    A = map(int, input().split())

    ans = sum(a for a in sorted(A, reverse=True)[::2])
    print(ans)


if __name__ == '__main__':
    main()
