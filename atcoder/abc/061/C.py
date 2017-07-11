def main():
    N, K = list(map(int, input().strip().split()))
    num_counts = {}
    for _ in range(N):
        a, b = list(map(int, input().strip().split()))
        if a in num_counts:
            num_counts[a] += b
        else:
            num_counts[a] = b

    num_counts = sorted(num_counts.items(),
                        key=lambda x: x[0])
    for n, c in num_counts:
        if K - c <= 0:
            print(n)
            break
        K -= c

if __name__ == '__main__':
    main()
