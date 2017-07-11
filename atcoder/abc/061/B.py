def main():
    N, M = list(map(int, input().strip().split()))
    load_counts = [0 for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().strip().split()))
        load_counts[a - 1] += 1
        load_counts[b - 1] += 1

    print("\n".join(map(str, load_counts)))

if __name__ == '__main__':
    main()
