def main():
    S_ = input()
    T = input()

    f(S_, T)


def f(s, t):
    l_t = len(t)
    for i in reversed(range(len(s)-l_t+1)):
        b = s[i:i+l_t]
        c = sum(c1 == c2 or c2 == "?" for c1, c2 in zip(t, b))

        if c == len(t):
            ans = s[:i].replace("?", "a") + t + s[i+l_t:].replace("?", "a")
            print(ans)
            return

    print("UNRESTORABLE")


if __name__ == '__main__':
    main()
