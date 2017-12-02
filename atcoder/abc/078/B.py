def main():
    X, Y, Z = map(int, input().split())
    # 人と人の間，また椅子の端と人の間には， 少なくとも Z センチメートル間を開ける必要があります。
    print((X - Z) // (Y + Z))

if __name__ == '__main__':
    main()
