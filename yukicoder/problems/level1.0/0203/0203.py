from itertools import groupby


def main():
    w1 = input()
    w2 = input()

    # RE: max, no args
    w = w1 + w2
    if w.count("o") == 0:
        print(0)
        return

    ans = max(len(list(g))
              for xo, g in groupby(w)
              if xo == "o")

    print(ans)

if __name__ == '__main__':
    main()
