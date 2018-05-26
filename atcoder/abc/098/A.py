def main():
    A, B = map(int, input().split())

    ans = max([
        A+B, A-B, A*B
    ])
    print(ans)


if __name__ == '__main__':
    main()
