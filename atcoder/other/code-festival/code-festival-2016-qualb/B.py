def main():
    N, A, B = map(int, input().split())
    S = input()

    AB = A+B
    n_passed = 0
    n_b = 0
    for s in S:
        passed = False
        if s == "a":
            if n_passed < AB:
                n_passed += 1
                passed = True
        elif s == "b":
            if n_passed < AB and n_b + 1 <= B:
                n_passed += 1
                n_b += 1
                passed = True

        if passed:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
