def main():
    N = int(input())
    total = 0
    for _ in range(N):
        l, r = map(int, input().split())
        total += r - l + 1
    print(total)

if __name__ == '__main__':
    main()
