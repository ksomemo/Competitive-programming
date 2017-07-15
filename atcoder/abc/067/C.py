def main():
    N = int(input().strip())
    a = list(map(int, input().strip().split()))
    min_v = float("inf")
    for i in range(1, N):
        x = sum(a[:i])
        y = sum(a[i:])
        min_v = min(min_v, abs(x - y))
    print(min_v)

if __name__ == '__main__':
    main()
