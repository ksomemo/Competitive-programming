def main():
    """
    op1: add 100 * A (water)
    op2: add 100 * B (water)
    op3: add C (sugar)
    op4: add D (sugar)

    each n_op -> 0 to inf

    (C*n_c + D*n_d): Water = E: 100
    """
    A, B, C, D, E, F = map(int, input().split())

    beaker = 0
    g_per_100 = E
    max_capacity = F
    total = 0
    sugar = 0

if __name__ == '__main__':
    main()
