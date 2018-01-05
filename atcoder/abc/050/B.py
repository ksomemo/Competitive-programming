def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    PX = [
        tuple(map(int, input().split()))
        for i in range(M)
    ]

    for p, x in PX:
        s = 0
        for i, t in enumerate(T, 1):
            if p == i:
                t = x
            s += t
        print(s)

if __name__ == '__main__':
    main()
