def main():
    S = input()
    T = input()

    ans = f(S, T)
    if ans:
        print("Yes")
    else:
        print("No")


def twi(S, T):
    """
    https://twitter.com/algon_320/status/1020670460441214976
    """
    return T in (S + S)


def f(S, T):
    for i in range(len(S)):
        t = S[-i:] + S[:-i]
        #print(S[-i:], S[:-i])
        if t == T:
            return True

    return False


if __name__ == '__main__':
    main()
