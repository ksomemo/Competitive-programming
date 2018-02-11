def main():
    S = input()

    ans = f(S)
    print(ans)


def f(S):
    """S[0].upper() + S[1:].lower()"""
    head = S[0]
    if ord(head) >= ord('a'):
        head = chr(ord(head) - 32)

    tail = map(ord, S[1:])
    tail = map(lambda o: o if o >= ord('a') else o + 32, tail)
    tail = map(chr, tail)

    return head + "".join(tail)

if __name__ == '__main__':
    main()
