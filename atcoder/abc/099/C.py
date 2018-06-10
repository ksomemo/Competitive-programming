def main():
    """
    1 <= N <= 10^5
    """
    N = int(input())

    ans = f(N)
    print(ans)


def f(N):
    """
    1: 1回
    6^n, 9^n: n回

    「ちょうど」払う

    N円ちょうど払うときの最小回数
    1円で払えばN円のときN回
    N円以下の組合せによる最小回数

    例:
        2〜5: 2,3,4,5
        6: 1
        7,8: 2,3
        9: 1
        10〜14: 2,3,4,5
        15: 2

        15=14+1
          =13+2
          =12+3
          =11+4
          =10+5
          = 9+6
    """
    x = [i for i in range(N+1)]
    x = [0] * (N+1)
    x[1] = 1
    a, b = 6, 9
    while a <= N or b <= N:
        if a <= N:
            x[a] = 1
        if b <= N:
            x[b] = 1
        a, b = a * 6, b * 9

    return WA2(N, x)
    return WA1(N, x)


def WA2(N, x):
    for i in range(2, N+1):
        m = 0
        k = i
        for j in range(i, 0, -1):
            print(i, j, x[j], "aaa")
            if x[j] > 0:
                # 払えるので、残り金額を引く
                c = k // j
                k -= c * j
                # 回数更新
                m += x[j] * c
            if k == 0:
                break
        x[i] = m

    print(x)
    ans = x[N]
    return ans


def WA1(N, x):
    e = N
    ans = 0
    for y, ok in list(enumerate(x))[::-1]:
        if ok:
            c = e // y
            ans += c
            print(e, y, c, sep="\t")
            e -= c * y
            if N == 0:
                break

    return ans


if __name__ == '__main__':
    main()
