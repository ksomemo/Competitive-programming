def main():
    n = int(input())

    a = [None] * (n + 3)
    a[1] = 0
    a[2] = 0
    a[3] = 1

    for i in range(4, n + 1):
        s = a[i - 1] + a[i - 2] + a[i - 3]
        a[i] = s % 10007

    print(a[n])

if __name__ == '__main__':
    main()
