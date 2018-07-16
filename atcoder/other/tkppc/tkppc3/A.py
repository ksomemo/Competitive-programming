def main():
    C1, A = input().split()
    C2, B = input().split()

    A, B = int(A), int(B)

    if C1 == C2:
        diff = abs(A - B)
    else:
        diff = A + B
    ans = diff // 15

    print(ans)


if __name__ == '__main__':
    main()
