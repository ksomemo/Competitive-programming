def main():
    W, H, C = input().split()
    W, H = int(W), int(H)

    l1 = ("BW" * 25)[:W]
    l2 = ("WB" * 25)[:W]
    if C == "W":
        l1, l2 = l2, l1

    for i in range(H):
        if i % 2 == 0:
            print(l1)
        else:
            print(l2)

if __name__ == '__main__':
    main()
