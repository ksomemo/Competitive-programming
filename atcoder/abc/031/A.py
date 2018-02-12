def main():
    A, D = map(int, input().split())

    ans = max(A, D) * (min(A, D) + 1)
    print(ans)


if __name__ == '__main__':
    main()
