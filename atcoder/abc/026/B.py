import math


def main():
    N = int(input())
    R = [int(input()) for _ in range(N)]

    r2 = 0
    for i,  r in enumerate(sorted(R, reverse=True)):
        sign = 1 if i % 2 == 0 else -1
        r2 += sign * (r ** 2)

    ans = r2 * math.pi

    print(ans)

if __name__ == '__main__':
    main()
