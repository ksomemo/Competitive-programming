def main():
    A, B = map(int, input().split())

    A = 14 if A == 1 else A
    B = 14 if B == 1 else B

    if A > B:
        print("Alice")
    elif A < B:
        print("Bob")
    else:
        print("Draw")

if __name__ == '__main__':
    main()
