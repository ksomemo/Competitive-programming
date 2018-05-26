def main():
    h, m = map(int, input().split())

    ans = (18 - h) * 60 - m
    print(ans)


if __name__ == '__main__':
    main()
