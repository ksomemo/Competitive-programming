def main():
    A = int(input())
    S = input()

    n = A
    S1 = "x" + S
    for c in S1:
        if c == "+":
            n += 1
        elif c == "-":
            n -= 1

        if n == 0:
            break

    if n == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
