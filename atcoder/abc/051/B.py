def main():
    """
    2 <= K <= 2500
    0 <= S <= 3K = 7500
    0 <= X,Y,Z <= K
    X+Y+Z=S

    2500**3: 15625 * (10^6) => 1.5625 * (10^10)
    Z = S - x - y
    x * y: 2500^2
    """
    K, S = map(int, input().split())

    ans = 0
    for x in range(0, K + 1):
        for y in range(0, K + 1):
            z = S - x - y
            if 0 <= z <= K:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()
