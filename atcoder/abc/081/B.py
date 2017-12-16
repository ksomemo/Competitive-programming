def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    while True:
        odd_count = [a for a in A if a % 2 != 0]
        if len(odd_count) >= 1:
            break

        ans += 1
        A = [a // 2 for a in A]

    print(ans)

if __name__ == '__main__':
    main()
