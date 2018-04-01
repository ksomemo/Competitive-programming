def main():
    A, B, C, D = map(int, input().split())

    ans = A * 1728 + B * 144 + C * 12 + D
    print(ans)


if __name__ == '__main__':
    main()
