def main():
    """最長: s + t

    abc
      abc

    abc
     abc

    abc
    abc
    """
    N = int(input())
    s = input()
    t = input()

    ans = s + t
    for i in range(1, N+1):
        if s[-i:] == t[:i]:
            ans = s[:-i] + s[-i:] + t[i:]

    print(len(ans))


if __name__ == '__main__':
    main()
