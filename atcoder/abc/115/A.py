def main():
    D = int(input())

    AC(D)


def AC(D):
    if D == 25:
        print("Christmas")
    elif D == 24:
        print("Christmas Eve")
    elif D == 23:
        print("Christmas Eve Eve")
    else:
        print("Christmas Eve Eve Eve")


def editorial(D):
    ans = "Christmas" + " Eve" * (25 - D)
    return ans


if __name__ == '__main__':
    main()
