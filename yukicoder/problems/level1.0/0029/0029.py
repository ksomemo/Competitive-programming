from collections import Counter
from itertools import chain


def main():
    N = int(input())

    gen = (input().split() for _ in range(N))
    c = Counter(chain.from_iterable(gen))

    n_up = 0
    total_rem = 0
    for count in c.values():
        quotient, rem = divmod(count, 2)
        n_up += quotient
        total_rem += rem

    print(n_up + total_rem // 4)

if __name__ == '__main__':
    main()
