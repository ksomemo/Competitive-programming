from itertools import product


def main():
    """
    A op1 B op2 C op3 D = 7
    op: +, -
    """

    _input = input()
    op1, op2, op3 = f(_input)
    A, B, C, D = list(_input)
    print(A + op1 + B + op2 + C + op3 + D + "=7")


def f(_input):
    A, B, C, D = map(int, list(_input))
    ans = 7 - A

    op = ("+", "-")
    op_p = product(op, op, op)
    bcd_p = product((B, -B), (C, -C), (D, -D))
    for ops, bcd in zip(op_p, bcd_p):
        if sum(bcd) == ans:
            return ops

if __name__ == '__main__':
    main()
