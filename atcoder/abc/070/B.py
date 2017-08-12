def main():
    A, B, C, D = list(map(int, input().strip().split()))
    print(calc(A, B, C, D))


def calc(A, B, C, D):
    # bがa包含
    # aがb包含
    # a start をbが包含
    # a end をbが包含
    if C <= A <= B <= D:
        return B - A
    elif A <= C <= D <= B:
        return D - C
    elif C <= A <= D:
        return D - A
    elif C <= B <= D:
        return B - C
    else:
        return 0

if __name__ == '__main__':
    main()
