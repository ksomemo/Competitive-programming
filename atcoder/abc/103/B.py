def main():
    S = input()
    T = input()

    ans = f(S, T)
    if ans:
        print("Yes")
    else:
        print("No")


def f(S, T):
    for i in range(len(S)):
        t = S[-i:] + S[:-i]
        #print(S[-i:], S[:-i])
        if t == T:
            return True

    return False


if __name__ == '__main__':
    main()
