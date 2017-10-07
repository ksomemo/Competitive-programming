from collections import Counter


def main():
    c = Counter(map(int, input().split()))

    if len(c.keys()) == 2 and max(c.values()) == 3:
        # WA: max忘れてfour cardを役と誤判断
        print("FULL HOUSE")
    elif max(c.values()) == 3:
        print("THREE CARD")
    elif len(c.keys()) == 3:
        print("TWO PAIR")
    elif max(c.values()) == 2:
        print("ONE PAIR")
    else:
        print("NO HAND")

if __name__ == '__main__':
    main()
