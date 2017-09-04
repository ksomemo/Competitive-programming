def main():
    # 100, 25, 1
    L = int(input())
    M = int(input())
    N = int(input())

    N_rem = N % 25
    M += N // 25

    M_rem = M % 4
    L += M // 4

    L_rem = L % 10

    print(sum([L_rem, M_rem, N_rem]))

if __name__ == '__main__':
    main()
