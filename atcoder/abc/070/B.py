def main():
    A, B, C, D = list(map(int, input().strip().split()))
    print(calc(A, B, C, D))


def calc(A, B, C, D):
    # bがa包含
    # aがb包含
    # a start をbが包含
    # a end をbが包含
    res = min(B, D) - max(A, C)
    if res < 0:
        return 0
    else:
        return res

if __name__ == '__main__':
    main()
