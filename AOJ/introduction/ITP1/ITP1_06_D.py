def main():
    n, m = map(int, input().split())
    matrix = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    vector = [
        int(input())
        for _ in range(m)
    ]

    for v in matrix:
        res = sum(x * y for x, y in zip(v, vector))
        print(res)

if __name__ == "__main__":
    main()
