def main():
    while True:
        m, f, r = map(int, input().split())
        if (m, f, r) == (-1, -1, -1):
            break

        if m == -1 or f == -1:
            print("F")
            continue

        m = m if m > -1 else 0
        f = f if f > -1 else 0
        r = r if r > -1 else 0
        mf = m + f

        if mf >= 80:
            print("A")
        elif 65 <= mf < 80:
            print("B")
        elif 50 <= mf < 65:
            print("C")
        elif 30 <= mf < 50:
            if r >= 50:
                print("C")
            else:
                print("D")
        else:
            print("F")


if __name__ == "__main__":
    main()
