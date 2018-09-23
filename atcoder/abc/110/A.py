def main():
    A, B, C = map(int, input().split())

    n = sorted([A, B, C])
    ans = n[0] + n[1] + n[2] * 10
    print(ans)


if __name__ == '__main__':
    main()
