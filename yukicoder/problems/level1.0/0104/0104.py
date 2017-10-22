from functools import reduce


def main():
    S = input()

    def f(value, element):
        if element == "L":
            return 2 * value
        else:
            return 2 * value + 1
    ans = reduce(f, S, 1)

    print(ans)

if __name__ == '__main__':
    main()
