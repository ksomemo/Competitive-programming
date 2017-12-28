def main():
    A, B, C = map(int, input().split())

    rem = set()
    s = 0
    i = 1
    while True:
        s += A * i
        m = s % B
        if m == C:
            print("YES")
            break

        if m in rem:
            print("NO")
            break

        rem.add(m)

if __name__ == '__main__':
    main()
