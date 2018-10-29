def main():
    A = int(input())
    B = int(input())
    C = int(input())
    S = int(input())

    t = A + B + C
    if t <= S <= t + 3:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
