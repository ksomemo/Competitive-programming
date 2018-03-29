def main():
    """
    100 ≤ N < 10^100000 
    """
    N = input()

    s = N[3:]
    e = len(s) + 2
    m = int(N[:3]) / 10
    m = int(m + 0.5) / 10
    if m >= 10:
        m /= 10
        e += 1

    ans = "{0}*10^{1}".format(m, e)
    print(ans)

if __name__ == '__main__':
    main()
