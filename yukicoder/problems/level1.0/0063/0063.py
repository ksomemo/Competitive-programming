def main():
    L, K = map(int, input().split())

    quotient, rem = divmod(L, 2 * K)
    if quotient == 0:
        ans = 0
    elif rem == 0:
        ans = (quotient - 1) * K
    else:
        ans = quotient * K
    print(ans)

if __name__ == '__main__':
    main()
