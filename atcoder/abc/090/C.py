def main():
    N, M = map(int, input().split())

    f(N, M)


def f(N, M):
    """
    カードAおよび周り8方向を裏返す
    すべてのカードについて行う
    うらの数(1)の枚数

    1 <= N,M <= 10^9
        シミュレート: TLE
    """
    # 紙でシミュレーションして得た法則
    """
    □□□□
    □■■□
    □■■□
    □□□□
    """
    ans = 0
    if N == 1 and M == 1:
        ans = 1
    elif N == 2 or M == 2:
        ans = 0
    elif N >= 3 and M >= 3:
        ans = (N-2) * (M-2)
    else:
        # 3>,1 or 1,3>
        ans = max(N, M) - 2

    print(ans)


if __name__ == '__main__':
    main()
