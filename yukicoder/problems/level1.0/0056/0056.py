import math


def main():
    D, P = map(int, input().split())
    tax_included_price = D * (100 + P) / 100
    print(math.floor(tax_included_price))

if __name__ == '__main__':
    main()
