def main():
    """
    1 <= i <= N
    p_1 ... p_n
    p_i != p_j
    2 <= N <= 10^5

    p_i != i にする
    最悪、sort(reverse) + αすれば終わりそう
    -> N^2(10^5^2 -> 10^10 NG)
    """
    N = int(input())
    p = list(map(int, input().split()))
    n_swap = 0

    for i in range(N - 1):
        for j in range(i, N - 1):
            if p[j] == j + 1 or p[j + 1] == j + 2:
                p[j + 1], p[j] = p[j], p[j + 1]
                n_swap += 1

    print(n_swap)

if __name__ == '__main__':
    main()
