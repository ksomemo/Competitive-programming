def main():
    K, N, F = map(int, input().split())
    A = map(int, input().split())
    rest_beans = K * N - sum(A)
    if rest_beans >= 0:
        print(rest_beans)
    else:
        print(-1)

if __name__ == '__main__':
    main()
