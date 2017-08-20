import string


def main():
    S = input()
    _str = set(S)
    lower_set = set(string.ascii_lowercase)
    if _str == lower_set:
        print("None")
    else:
        no_exists = list(lower_set - _str)
        print(sorted(no_exists)[0])


if __name__ == '__main__':
    main()
