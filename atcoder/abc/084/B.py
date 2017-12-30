def main():
    A, B = map(int, input().split())
    S = input()

    valid = False
    if S.count("-") == 1:
        s_a, s_b = S.split("-")
        if len(s_a) == A and len(s_b) == B:
            valid = True

    if valid:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
