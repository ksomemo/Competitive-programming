def main():
    # not use N
    _ = int(input().strip())

    points = list(map(int, input().strip().split()))
    min_p = min(points)
    max_p = max(points)
    print(max_p - min_p)

if __name__ == '__main__':
    main()
