def main():
    N = int(input())
    K = int(input())

    v = 1
    for _ in range(N):
        a = v * 2
        b = v + K
        v = min(a, b)

    print(v)

if __name__ == '__main__':
    main()
