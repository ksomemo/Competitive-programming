from collections import Counter


def main():
    N = int(input())
    S = input().split()

    c = Counter(S)

    n_types = len(c.keys())
    if n_types == 3:
        print("Three")
    elif n_types == 4:
        print("Four")


if __name__ == '__main__':
    main()
