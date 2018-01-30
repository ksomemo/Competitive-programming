import math


def main():
    a, b = input().split()

    f1(a, b)


def f1(a, b):
    c = a + b
    d = int(c)
    sqrt = math.sqrt(d)

    if int(sqrt) == sqrt:
        print("Yes")
    else:
        print("No")


def f2(a, b):
    c = a + b
    d = int(c)
    m = math.sqrt(100100)
    for i in range(11, int(m) + 1):
        if i * i == d:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    main()
