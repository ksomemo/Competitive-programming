def main():
    W, H = map(int, input().split())

    if W % 16 == 0 and H % 9 == 0:
        print("16:9")
    else:
        print("4:3")

if __name__ == '__main__':
    main()
