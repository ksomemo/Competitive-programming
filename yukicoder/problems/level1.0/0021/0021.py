def main():
    N = int(input())
    K = int(input())
    ns = [int(input()) for _ in range(N)]

    print(max(ns) - min(ns))

if __name__ == '__main__':
    main()
