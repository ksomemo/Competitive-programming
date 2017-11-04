def main():
    C1 = input()
    C2 = input()

    if C2 == C1[::-1] and C1 == C2[::-1]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
