def main():
    N, S, T = map(int, input().split())
    W = int(input())
    A = [int(input()) for _ in range(N-1)]

    # 初日忘れ
    ans = int(S <= W <= T)
    w1 = W
    for a in A:
        w1 += a
        if S <= w1 <= T:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
