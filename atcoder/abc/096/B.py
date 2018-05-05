def main():
    A, B, C = map(int, input().split())
    K = int(input())

    x, y, z = sorted([A, B, C])
    for i in range(K):
        z *= 2
    ans = x + y + z
    print(ans)


if __name__ == '__main__':
    main()
