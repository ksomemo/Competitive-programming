import math


def main():
    K = int(input())
    S = int(input())

    # x * (100 - K)% = S
    ans = S / ((100 - K) / 100)
    print(math.floor(ans))

if __name__ == '__main__':
    main()
