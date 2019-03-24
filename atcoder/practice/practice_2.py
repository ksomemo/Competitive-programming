import string


def main():
    N, Q = map(int, input().split())

    sample(N, Q)


def sample(N, Q):
    s = list(string.ascii_uppercase[:N])
    for _ in range(N):
        for j in range(N-1):
            print("? {} {}".format(s[j], s[j + 1]), flush=True)

            ans = input()
            if ans.strip() == '>':
                s[j], s[j + 1] = s[j + 1], s[j]

    print("! {}".format("".join(s)), flush=True)


def f(N, Q):
    pass


if __name__ == "__main__":
    main()
