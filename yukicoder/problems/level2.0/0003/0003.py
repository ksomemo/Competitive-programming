def main():
    N = int(input())

    square = 1
    ans = 1
    s_f = set()
    s_b = set()
    while True:
        if square == N:
            print(ans)
            return

        # forward/backward
        n_b1 = bin(square).count("1")
        square_f = square + n_b1
        square_b = square - n_b1
        if square_f > N:
            s_f.add(square)
        if square_b <= 0:
            s_b.add(square)

        if square in s_f and square in s_b:
            print(-1)
            return

        if square not in s_f:
            if square in square_b:
                ans -= 1
            s_f.add(square)
            square = square_f
        elif square not in s_b:
            if square in square_f:
                ans -= 1
            s_b.add(square)
            square = square_b

        ans += 1

if __name__ == '__main__':
    main()
