def main():
    B = map(int, input().split())
    for i, b in enumerate(B, 1):
        if i != b:
            print(i)
            return
    print(10)

if __name__ == '__main__':
    main()
