def main():
    A, B = map(int, input().split())

    ans = (B+A-1)//A
    print(ans)


if __name__ == '__main__':
    main()
