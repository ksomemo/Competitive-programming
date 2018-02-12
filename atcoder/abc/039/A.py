def main():
    A, B, C = map(int, input().split())

    ans = (A*B+B*C+C*A)*2
    print(ans)


if __name__ == '__main__':
    main()
