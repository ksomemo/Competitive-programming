def main():
    while True:
        H, W = map(int, input().split())
        if (H, W) == (0, 0):
            break

        print("#" * W)
        for _ in range(H - 2):
            print("#" + "." * (W - 2) + "#")
        print("#" * W)
        print("")

if __name__ == "__main__":
    main()
