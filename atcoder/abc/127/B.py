def main():
    """
    x(i+1)=r * x(i)−D
    2001
    2010
    """
    r, D, x2000 = map(int, input().split())

    bef_x = x2000
    for _ in range(2001, 2010+1):
        ans = r * bef_x - D
        bef_x = ans
        print(ans)


if __name__ == '__main__':
    main()
