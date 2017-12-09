def main():
    s = input()
    q = int(input())

    for _ in range(q):
        query = input().split()
        op, a, b = query[0:3]
        a, b = int(a), int(b)

        if op == "replace":
            p = query[3]
            s = s[:a] + p + s[b + 1:]
        elif op == "reverse":
            s = s[:a] + s[a:b + 1][::-1] + s[b + 1:]
        elif op == "print":
            print(s[a:b + 1])


if __name__ == "__main__":
    main()
