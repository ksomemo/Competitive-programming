def main():
    N = int(input())

    # AC(N)
    editorial2(N)


def AC(N):
    print(N)
    for i in range(N):
        print(1)


def editorial2(N):
    c = 0
    elms = []

    # N_max:10 より 1010
    for i in range(4):
        if (N >> i) & 1:
            c += 1
            elms.append(1 << i)

    print(c)
    for e in elms:
        print(e)


if __name__ == '__main__':
    main()
