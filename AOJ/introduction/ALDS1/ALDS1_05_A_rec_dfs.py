def main():
    n = 4
    l = [0] * n

    def rec(i):
        if i == n:
            print(l)
            return

        rec(i + 1)
        l[i] = 1
        rec(i + 1)
        l[i] = 0

    rec(0)

if __name__ == '__main__':
    main()
