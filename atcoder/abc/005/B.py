def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]

    ans = sorted(T)[0]
    print(ans)

if __name__ == '__main__':
    main()
