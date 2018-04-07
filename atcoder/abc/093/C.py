def main():
    A,B,C = map(int, input().split())

    f(A,B,C)


def f(A,B,C):
    """
    A: 545, 565, 666 ans=2
    B: 445,      555 ans=1
    C: 123, 233, A pattern ans=3
    D: 135, 245, 355, 555 ans=3
    E: 235, 345, 455, A pattern ans=4
    """
    A, B, C = sorted([A, B, C])
    ans = 0
    if B != C:
        ans += C - B
        B = C
        A += ans
    
    diff = B - A
    ans += diff // 2
    if diff % 2 != 0:
        # A+2,BC+1
        ans += 2

    print(ans)


if __name__ == '__main__':
    main()
