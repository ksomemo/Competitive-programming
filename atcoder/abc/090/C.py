def main():
    N, M = map(int, input().split())

    f(N, M)


def editorial(N, M):
    """
    1:四隅, 2:辺(四隅以外の端), 3:それ以外について何回裏返すかを考える
    1: 対象+上下斜め  合計4回裏返す 偶奇を考えると表のまま
    1: 対象+中央+隣接 合計6回裏返す 偶奇を考えると表のまま
    1: 対象+8方法    合計9回裏返す 偶奇を考えると裏
    """
    pass


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
