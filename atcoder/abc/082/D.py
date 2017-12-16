def main():
    """
    Tの命令 組合せ: 2^N_T
    max_N_T: 8000

    |x|,|y|<=8000
    -> (x,y) 組合せ: 10^8 < 16,000^2 < 10^9
    """
    s = input()
    x, y = map(int, input().split())

    solve(s, x, y)


def solve(s, x, y):
    pos_x, pos_y = 0, 0
    dir_x, dir_y = 1, 0
    for q in s:
        if q == "F":
            pos_x += dir_x
            pos_y += dir_y
        else:
            pass

    if (pos_x, pos_y) == (x, y):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
