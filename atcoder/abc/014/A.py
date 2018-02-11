def main():
    a = int(input())
    b = int(input())

    m = a % b
    if m == 0:
        print(0)
    else:
        print(b - m)

if __name__ == '__main__':
    main()
