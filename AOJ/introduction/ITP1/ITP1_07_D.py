def main():
    n, m, l = map(int, input().split())

    nm_mat = [
        [int(x) for x in input().split()]
        for _ in range(n)
    ]
    ml_mat = [
        [int(x) for x in input().split()]
        for _ in range(m)
    ]
    nl_mat = [
        [0] * l
        for _ in range(n)
    ]

    for i_n, row in enumerate(nm_mat):
        for i_l in range(l):
            col = [ml_mat[i_m][i_l] for i_m in range(m)]
            inner_product = sum(x * y for x, y in zip(row, col))

            nl_mat[i_n][i_l] = inner_product

    for row in nl_mat:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
