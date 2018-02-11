def main():
    M, D = map(int, input().split())

    ans = ("NO", "YES")[M % D == 0]
    print(ans)

if __name__ == '__main__':
    main()
