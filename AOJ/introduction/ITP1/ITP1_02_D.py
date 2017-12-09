def main():
    W, H, x, y, r = map(int, input().split())

    x1 = x - r
    x2 = x + r
    y1 = y - r
    y2 = y + r
    if 0 <= x1 <= W and \
            0 <= x2 <= W and \
            0 <= y1 <= H and \
            0 <= y2 <= H:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
