import math
from collections import Counter


def main():
    S = input()
    c = Counter(S)
    v = abs(c.get("N", 0) - c.get("S", 0))
    h = abs(c.get("W", 0) - c.get("E", 0))

    ans = math.sqrt(v ** 2 + h ** 2)
    print(ans)

if __name__ == '__main__':
    main()
