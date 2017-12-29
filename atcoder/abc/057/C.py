import math


def main():
    N = int(input())

    # 1 * N
    ans = len(str(N))
    sqrt_N = int(math.sqrt(N))
    for i in range(2, sqrt_N + 1):
        if N % i == 0:
            d = N // i
            res = max(len(str(d)), len(str(i)))
            ans = min(ans, res)

    print(ans)

if __name__ == '__main__':
    main()
