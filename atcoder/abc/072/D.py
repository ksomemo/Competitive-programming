def main():
    """
    1 <= i <= N
    p_1 ... p_n
    p_i != p_j
    2 <= N <= 10^5

    p_i != i にする
    最悪、sort(reverse) + αすれば終わりそう
    -> N^2(10^5^2 -> 10^10 NG)

    xx: 12(xx) -> 21(oo)
    xo: 132(xoo) -> 312(ooo)
    ox:
      oは飛ばしてxから始める
    """
    N = int(input())
    p = map(int, input().split())
    n_swap = 0

    p_same = [i == _p for i, _p in enumerate(p, 1)]
    # enumerateでは複製になるのでrangeで回しながら更新
    for i in range(N - 1):
        same = p_same[i]
        if same:
            n_swap += 1
            p_same[i] = p_same[i + 1] = False

    if p_same[-1]:
        n_swap += 1
    print(n_swap)

if __name__ == '__main__':
    main()
