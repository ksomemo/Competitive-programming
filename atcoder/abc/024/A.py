def main():
    A, B, C, K = map(int, input().split())
    S, T = map(int, input().split())

    ch = A * S
    ad = B * T
    ans = ch + ad
    if S + T >= K:
        ans -= (S + T) * C

    print(ans)

if __name__ == '__main__':
    main()
