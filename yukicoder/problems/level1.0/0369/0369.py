def main():
    N = int(input())
    A = map(int, input().split())
    v = int(input())

    print(sum(A) - v)

if __name__ == '__main__':
    main()
