import math


def main():
    a, b = map(int, input().split())

    ans = math.ceil((a + b) / 2)
    print(ans)

if __name__ == '__main__':
    main()
