from collections import Counter
import string


def main():
    """
    各文字列の共通文字とその最大文字数を求め
    並べてsort
    """
    n = int(input())

    inf = float("inf")
    d = {k: inf for k in string.ascii_lowercase}
    for i in range(n):
        S = input()
        c = Counter(S)
        for char, n_char in d.items():
            d[char] = min(d[char], c.get(char, 0))

    ans = ""
    for k, v in d.items():
        if v == inf:
            continue
        ans += k * v
    ans = "".join(sorted(ans))

    print(ans)

if __name__ == '__main__':
    main()
