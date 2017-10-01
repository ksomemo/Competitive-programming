def main():
    # 4:3 or 3:4
    H, W = map(int, input().split())

    if H > W:
        print('TATE')
    else:
        print("YOKO")

if __name__ == '__main__':
    main()
