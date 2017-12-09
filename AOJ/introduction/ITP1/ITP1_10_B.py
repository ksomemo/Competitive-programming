import math


def main():
    a, b, C = map(int, input().split())

    # 三角形より、 0 < C < 180
    rad = math.pi * C / 180
    sin = math.sin(rad)
    h = b * sin
    S = a * h / 2

    a_ = a - math.cos(rad)
    len_d = math.sqrt(a_ ** 2 + h ** 2)

    print(S)
    print(a + b + len_d)
    print(h)

if __name__ == "__main__":
    main()
