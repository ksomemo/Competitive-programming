def main():
    K = int(input())

    d = {}
    for i in range(1, K+1):
        for j in range(i+1, K+1):
            p = tuple(sorted((i, j)))
            if i % 2 == 1 and j % 2 == 0:
                d[p] = 1
            elif i % 2 == 0 and j % 2 == 1:
                d[p] = 1

    ans = len(d)
    print(ans)


if __name__ == '__main__':
    main()
