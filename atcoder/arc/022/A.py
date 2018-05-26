def main():
    S = input()

    s = S.upper()
    if AC(s):
        print("YES")
    else:
        print("NO")


def test_ans():
    ss = [
        "InformationAndCommunicationTechnology",
        "InformationTechnology",
        "SinCosTan",
        "Ticket",
        "InternetTrouble",
    ]
    for s in ss:
        assert AC(s) == o1(s) == o2(s) == o3(s)


def AC(s):
    if "I" in s:
        i = s.index("I")
        s = s[i+1:]
        if "C" in s:
            i = s.index("C")
            s = s[i+1:]
            if "T" in s:
                return True

    return False


def o1(s):
    if "I" not in s:
        return False

    i = s.index("I")
    if "T" not in s:
        return False

    j = len(s) - 1 + s[::-1].index("T")

    return "C" in s[i:j+1]


def o2(s):
    n = len(s)
    for i in range(n):
        if s[i] == "C":
            if "I" in s[:i] and "T" in s[i+1:]:
                return True

    return False


def o3(s):
    n = len(s)
    for i in range(n):
        c1 = s[i]
        for j in range(i+1, n):
            c2 = s[j]
            for k in range(j+1, n):
                c3 = s[k]
                if [c1, c2, c3] == list("ICT"):
                    return True

    return False


if __name__ == '__main__':
    main()
