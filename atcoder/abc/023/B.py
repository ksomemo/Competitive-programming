def main():
    N = int(input())
    S = input()

    b = "b"
    if S == b:
        print(0)
        return

    for i in range(1, N+1):
        if i % 3 == 1:
            b = "a" + b + "c"
        elif i % 3 == 2:
            b = "c" + b + "a"
        else:
            b = "b" + b + "b"

        if b == S:
            print(i)
            return

    print(-1)


if __name__ == '__main__':
    main()
