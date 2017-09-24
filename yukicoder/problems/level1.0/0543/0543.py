def main():
    a, b = input().split()
    # p: proposition(命題)
    # b: back(裏)
    # rev: reverse(逆)
    # c: contraposition(対偶)
    p = a
    p_rev = b
    p_c = p
    p_rev_c = p_rev
    p_b = p_rev_c

    print(p_b, p_c)

if __name__ == '__main__':
    main()
