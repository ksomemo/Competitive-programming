def main():
    """
    一番多い数の種類のケーキから食べる
    上記と異なる種類のケーキのうち、一番多い数の種類のケーキを食べる
    以下繰り返し
        他のケーキの個数がすべて0なら連続日数として追加
    """
    K, T = map(int, input().split())
    A = map(int, input().split())

    A = list(A)
    f(K, T, A)


def f2(K, T, A):
    """
    ある１種類が他の種類より2倍より多いとNG
    愚直にシミュレーションしなくてもと考えたが間違い
    →editorial参照

    3 2 2: abacabc
        3は他の4つで挟めば良い
    3 2 1: 上記の末尾抜き
        3は他の3つと交互に食べれば良い
    4 2 1: ababaca
        4, ceil(7/2)=4
    5 2 1: ababaca a
        余る
    """
    pass


def editorial(K, T, A):
    """
    一番多いtype:tの数が3のとき
    t_t_t
    他の数は間にn-1個入れることができる
    入れなければn-1回重複
    1つ入れると1減る
    max_a以外の個数はK-max_a
    """
    max_a = max(A)

    ans = max(max_a − 1 − (K − max_a), 0)
    print(ans)


def f(K, T, A):
    cake_type = None
    rest_K = K
    ans = 0
    while rest_K > 0:
        bef_cake_type = cake_type
        max_a = 0
        for i, a in enumerate(A):
            if a > max_a and i != bef_cake_type:
                cake_type = i
                max_a = a

        A[cake_type] -= 1
        rest_K -= 1
        if bef_cake_type == cake_type:
            ans += 1
        # print(A, "cur:", cake_type, "bef:", bef_cake_type, sep="\t")

    print(ans)


if __name__ == '__main__':
    main()
