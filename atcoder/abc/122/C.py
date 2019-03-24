def main():
    N, Q = map(int, input().split())
    S = input()
    lr = [
        list(map(int, input().split()))
        for _ in range(Q)
    ]

    a = [0] * (N + 1)
    for i in range(1, N+1):
        a[i] = a[i-1]
        if S[i-2:i] == "AC":
            a[i] += 1

    # print(a)
    ans = 0
    for l, r in lr:
        ans = a[r] - a[l]
        print(ans)


if __name__ == '__main__':
    main()
