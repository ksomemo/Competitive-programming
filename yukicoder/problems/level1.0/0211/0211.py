from itertools import product


def main():
    K = int(input())

    ps = [2, 3, 5, 7, 11, 13]
    cs = [4, 6, 8, 9, 10, 12]
    # Composite number
    a = sum(p * c == K
            for (p, c) in product(ps, cs))

    print(a / 36)

if __name__ == '__main__':
    main()
