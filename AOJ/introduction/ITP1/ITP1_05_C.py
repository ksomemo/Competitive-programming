def main():
    line1 = "#." * 150
    line2 = ".#" * 150
    while True:
        H, W = map(int, input().split())
        if (H, W) == (0, 0):
            break

        for i in range(H):
            if i % 2 == 0:
                print(line1[:W])
            else:
                print(line2[:W])
        print("")

if __name__ == "__main__":
    main()
