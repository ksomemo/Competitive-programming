def main():
    S = input()
    T = input()

    for s, t in zip(S, T):
        if s == t:
            continue
        if not f(s, t):
            print("You will lose")
            return

    print("You can win")


def f(s, t):
    c = "atcoder"
    if s == "@" and t in c:
        return True
    elif t == "@" and s in c:
        return True

    return False


def editorial(s, t):
    d = {c: 1 for c in "atcoder"}
    d["@"] = 10

    # @ + atcoder = 11
    score = d.get(s, 0) + d.get(t, 0)
    return score >= 11


if __name__ == '__main__':
    main()
