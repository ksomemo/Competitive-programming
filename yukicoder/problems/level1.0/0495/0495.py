from collections import Counter


def main():
    S = input()
    c = count1(S)
    print(" ".join(map(str, c)))


def count1(S):
    c = Counter(S[:-1].split(")"))
    return c.get("(^^*", 0), c.get("(*^^", 0)


def count2(S):
    return S.count("(^^*)"), S.count("(*^^)")

if __name__ == '__main__':
    main()
