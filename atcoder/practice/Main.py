from functools import reduce
import operator


def main():
    a = input()
    b, c = input().split(" ")
    s = input()

    sum = reduce(operator.add, map(int, [a, b, c]))
    print(str(sum) + " " + s)


if __name__ == '__main__':
    main()
