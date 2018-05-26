def main():
    N = int(input())

    m = int(N ** 0.5)
    for i in range(2, m+1):
        if N % i == 0:
            print("NO")
            return

    print("YES")


if __name__ == '__main__':
    main()
