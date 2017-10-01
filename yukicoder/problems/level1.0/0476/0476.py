def main():
    n, a = map(int, input().split())
    x = map(int, input().split())

    if sum(x) == n * a:
        print('YES')
    else:
        print("NO")

if __name__ == '__main__':
    main()
