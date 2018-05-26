def main():
    L, X, Y, S, D = map(int, input().split())

    v1 = X + Y
    v2 = Y - X
    if S < D:
        x1 = D - S
        x2 = L - x1
    else:
        x2 = S - D
        x1 = L - x2

    if S == D:
        print(0)
        return

    # 注意
    if v2 < 0:
        x2 = x1
        v2 = abs(v2)
    
    t1 = abs(x1 / v1)
    if v2 == 0:
        t2 = float("inf")
    else:
        t2 = abs(x2 / v2)

    ans = min(t1, t2)
    print(ans)


if __name__ == '__main__':
    main()
