def main():
    N, M = map(int, input().split())

    for n in range(1, N+1):
        if n != M:
            print(n)
            return

if __name__ == '__main__':
    main()
