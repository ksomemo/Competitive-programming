def main():
    S = input()

    t = S.count("t")
    r = S.count("r")
    ee = S.count("e") // 2

    print(min(t, r, ee))

if __name__ == '__main__':
    main()
