def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for i in range(N - 2):
        a = A[i:i + 3]
        if len(set(a)) < 3:
            continue
        if max(a) == a[1] or min(a) == a[1]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
