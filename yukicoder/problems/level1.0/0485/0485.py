def main():
    A, B = map(int, input().split())

    if B % A == 0:
        print(B // A)
    else:
        print("NO")

if __name__ == '__main__':
    main()
