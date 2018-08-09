def main():
    S = input()

    ans = f(S)
    ans = regex(S)

    print(ans)


def f(S):
    if S[0] != "A":
        return "WA"

    nc = S[2:-1].count("C")
    if nc != 1:
        return "WA"

    import string
    for c in S[1] + S[-1]:
        if c in string.ascii_uppercase:
            return "WA"

    return "AC"


def regex(S):
    import re

    r = re.compile("^A[a-z][^C]*C[^C]*[a-z]$")
    if r.match(S):
        return "AC"
    else:
        return "WA"


if __name__ == '__main__':
    main()
