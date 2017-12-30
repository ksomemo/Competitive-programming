def main():
    N = int(input())

    p = 1
    for i in range(1, N + 1):
        # TLE
        # p *= i
        p = (p * i) % (10 ** 9 + 7)

    ans = p % (10 ** 9 + 7)
    print(ans)

if __name__ == '__main__':
    main()
