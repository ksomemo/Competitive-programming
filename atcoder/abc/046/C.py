def main():
    N=int(input())
    TA = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    ans = f(N, TA)
    print(ans)

def f(N, TA):
    nt = TA[0][0]
    na = TA[0][1]

    bef_t, bef_a = nt, na
    for t, a in TA[1:]:
        if (bef_t, bef_a) == (t, a):
            continue

        if bef_t == t and bef_a < a:
            na = a
        # nt + x: na + y = t: a
        # na * t + y * t = nt * a + x * a
        # y = ([nt + x] * a) / t - na
        # 0<=x,y
        nt = t
        na = a

    ans = t + a 
    return ans


if __name__ == '__main__':
    main()
