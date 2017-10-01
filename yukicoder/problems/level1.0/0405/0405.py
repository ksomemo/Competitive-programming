def main():
    S1, T = input().split()
    T = int(T)

    short_hand = r2a(S1)
    short_hand = (short_hand + T) % 12
    if short_hand == 0:
        short_hand = 12

    print(a2r(short_hand))


def r2a(r):
    i_count = r.count("I")
    if r[0] == "V":
        a = 5 + i_count
    elif r[0] == "X":
        a = 10 + i_count
    elif r[-1] == "X":
        a = 10 - i_count
    else:
        a = i_count

    return a


def a2r(a):
    if a >= 10:
        r = "X" + "I" * (a % 10)
    elif a == 9:
        r = "IX"
    elif a >= 5:
        r = "V" + "I" * (a - 5)
    else:
        r = "I" * a

    return r

if __name__ == '__main__':
    main()
