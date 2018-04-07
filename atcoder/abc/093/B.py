def main():
    A, B, K = map(int, input().split())

    end = min(A+K, B)
    for i in range(A, end):
        print(i)

    start = B-K+1
    if end >= start:
        start = end
    for i in range(start, B+1):
        print(i)


if __name__ == '__main__':
    main()
