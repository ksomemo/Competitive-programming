def main():
    N, A, B = map(int, input().split())

    ans = min(N * A, B)
    print(ans)

if __name__ == '__main__':
    main()
